from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile
from pprint import pprint

class PostSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    # category = serializers.SlugRelatedField(many=False, queryset=Category.objects.all(), slug_field='name')
    snippet = serializers.CharField(read_only=True, source='get_snippet')
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'absolute_url', 'author', 'image', 'title', 'snippet', 'content', 'category', 'publish_date']
        read_only_fields = ['author']


    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        # pprint(request.__dict__)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('absolute_url')
            
        else:
            rep.pop('content')   
            rep.pop('image')   
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep
    
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']
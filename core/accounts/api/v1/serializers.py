from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        
        
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'details': 'passwords dosent match'})
        
        try:
            password_validation.validate_password(attrs.get('password'))
        except ValidationError as e:
                raise serializers.ValidationError({'password': e.messages})
        
        return super().validate(attrs)



    def create(self, validated_data):
        validated_data.pop('password1', None)
        
        return User.objects.create_user(**validated_data)

        
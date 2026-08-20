from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

"""
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'POST':
        ser_data = PostSerializer(data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        Response(ser_data.data, status=status.HTTP_201_CREATED)


    posts = Post.objects.filter(status=True)
    ser_data =  PostSerializer(posts, many=True)
    return Response(ser_data.data)
"""
      
    
"""
@api_view(['GET','PUT', 'Delete'])
# @permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    
    if request.method == 'PUT':  
        ser_data = PostSerializer(post, data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        Response(ser_data.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        post.delete()
        return Response('item removed successfuly')
    
    ser_data = PostSerializer(post)
    return Response(ser_data.data)
    """
    
    
# class PostListView(APIView):
#     posts = Post.objects.filter(status=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     def get(self, request):
#         ser_data = PostSerializer(self.posts, many=True) 
#         return Response(ser_data.data)


#     def post(self, request):
#         ser_data = PostSerializer(data=request.data)
#         ser_data.is_valid(raise_exception=True)
#         ser_data.save()
#         return Response(ser_data.data)



class PostDetailView(APIView):
    '''
    getting and creatting post.
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True) 
    #    post = get_object_or_404(self.post, pk=pk, status=True) 
        ser_data = PostSerializer(post)
        return Response(ser_data.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True) 
        ser_data = PostSerializer(post, data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response(ser_data.data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True) 
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self):
    #     queryset = Post.objects.filter(status=True)
    #     return queryset

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    
# class PostViewSet()
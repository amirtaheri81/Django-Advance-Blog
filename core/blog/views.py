from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    
class PostDetailView(DetailView):
    model = Post
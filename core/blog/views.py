from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    
class PostDetailView(DetailView):
    model = Post
    
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/add/'
      
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    
  
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/'
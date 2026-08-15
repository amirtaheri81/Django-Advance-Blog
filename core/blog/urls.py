from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_datail'),
    path('post/add/', views.PostCreateView.as_view(), name='post_add'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/del/', views.PostDeleteView.as_view(), name='post_delete')
]
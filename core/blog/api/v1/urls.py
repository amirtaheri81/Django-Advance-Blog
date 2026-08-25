from django.urls import path
from rest_framework import routers
from . import views

app_name = 'api-v1' 


router = routers.DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('category', views.CategoryViewSet, basename='category')
urlpatterns = router.urls


# urlpatterns = [
#     # path('', views.PostListView.as_view(), name='post-list'),
#     # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
#     path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put':'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='post_detail')
# ]
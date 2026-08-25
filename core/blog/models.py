from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Profile

# getting user model object
user = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    
    
    def get_snippet(self):
        return self.content[:5]
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
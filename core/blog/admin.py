from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'status', 'author', 'create_date', 'update_date')
        list_editable = ['status']

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
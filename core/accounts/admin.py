from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_active', 'is_superuser')
    # search_fields = ("email",)
    ordering = ("email",)
    model = User
    fieldsets = (
    ('Authentication', {
        "fields": ("email", "password")}),
    ("Permissions", {
        "fields": ("is_staff", "is_active",)}),
    ("Group Permissions", {
        "fields": ("groups", "user_permissions",)}),
    ("Important Date", {
        "fields": ("last_login",)}),
    ) 
    add_fieldsets = (
        ('Authentication', {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", 'is_superuser'
            )}
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
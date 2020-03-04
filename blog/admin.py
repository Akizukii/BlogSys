from django.contrib import admin

# Register your models here.
from .models import Admin, Category, Post, Comment

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
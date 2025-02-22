from django.contrib import admin
from .models import Post, Reply

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'created_at')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'post', 'created_at')
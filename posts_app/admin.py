from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'views', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['views', 'created_at', 'updated_at']


admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title parent'.split()
    list_filter = 'parent'.split()
    search_fields = 'title'.split()
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

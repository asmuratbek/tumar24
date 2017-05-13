from django.contrib import admin
from .models import *


# Register your models here.

class MetroAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class CityAdmin(admin.ModelAdmin):
    search_fields = ['title']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['text']

admin.site.register(Metro, MetroAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(AboutUs, AboutAdmin)

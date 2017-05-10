from django.contrib import admin
from .models import *


# Register your models here.

class MetroAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class CityAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Metro, MetroAdmin)
admin.site.register(City, CityAdmin)

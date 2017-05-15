from django.contrib import admin
from .models import *

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ['link', 'content', 'life_time', 'title', 'is_active']
    list_filter = ['life_time']
    search_fields = ['link', 'title']

admin.site.register(VerticalBanners, BannerAdmin)
admin.site.register(HorizontalBanners, BannerAdmin)


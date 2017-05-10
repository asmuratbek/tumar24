# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ad_app.models import *


# Register your models here.

class AdAdmin(admin.ModelAdmin):
    list_display = 'title price city category'.split()
    list_filter = 'category created_at'.split()


admin.site.register(Ad, AdAdmin)
admin.site.register(Coordinates)
admin.site.register(Comment)
admin.site.register(Media)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from categories.views import generate_view_params
from .models import *

from django.shortcuts import render

# Create your views here.


def one_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    params = {
        'ad': ad
    }
    params.update(generate_view_params(request))
    return render(request, 'app/one_ad.html', params)

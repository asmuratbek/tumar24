# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse

from categories.views import generate_view_params
from .models import *
from .forms import AdCreationForm, SearchForm
from django.shortcuts import render


# Create your views here.


def one_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    prev_id = Ad.objects.filter(id__lt=ad_id).order_by('id').last()
    next_id = Ad.objects.filter(id__gt=ad_id).order_by('id').first()
    params = {
        'ad': ad,
        'prev': prev_id.id if prev_id else None,
        'next': next_id.id if next_id else None
    }
    params.update(generate_view_params(request))
    return render(request, 'app/one_ad.html', params)


def all_ads(request):
    paginator = Paginator(Ad.objects.all(), 12)
    page = int(request.GET.get('page', 1))
    ads = paginator.page(page)

    params = {
        'ads': ads,
        'pagination': ads,
        'page_range': ads
    }
    params.update(generate_view_params(request))
    return render(request, 'app/all_ads.html', params)


def create_new_ad(request):
    form = AdCreationForm(request.POST)
    if request.POST:
        if form.is_valid():
            print form.cleaned_data
            return JsonResponse(dict(message='We\'v got a request for adding new ad'))
        else:
            print form.errors
            return HttpResponse(str(form.errors))
    return JsonResponse(dict(message='Request is post!'))


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        filters = dict()
        filters['title__icontains'] = form.cleaned_data['search_word'].lower()
        if form.cleaned_data['categories']:
            category = Category.objects.filter(id=int(form.cleaned_data['categories'])).first()
            filters['category'] = category

        if form.cleaned_data['metro']:
            metro = Metro.objects.filter(id=int(form.cleaned_data['metro'])).first()
            filters['metro'] = metro

        paginator = Paginator(Ad.objects.filter(**filters), 12)
        ads = paginator.page(request.GET.get('page', 1))

        params = {
            'ads': ads,
            'pagination': ads
        }
        params.update(generate_view_params(request))
        return render(request, 'app/all_ads.html', params)


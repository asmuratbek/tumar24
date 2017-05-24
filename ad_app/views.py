# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import threading

from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from geoposition import Geoposition
from Classified.parameters import SITE_PROTOCOL, SITE_URL, ADMIN_EMAIL
from categories.views import generate_view_params
from .models import *
from .forms import AdCreationForm, SearchForm
from django.shortcuts import render
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def one_ad(request, ad_id):
    try:
        ad = Ad.objects.get(id=ad_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('exception:not_found'))

    prev_id = Ad.objects.filter(id__lt=ad_id, is_active=True).order_by('id').last()
    next_id = Ad.objects.filter(id__gt=ad_id, is_active=True).order_by('id').first()
    hit_count = HitCount.objects.get_for_object(ad)
    response = HitCountMixin.hit_count(request, hit_count)
    if response.hit_counted:
        ad.views += 1
        ad.save()

    params = {
        'ad': ad,
        'prev': prev_id.id if prev_id else None,
        'next': next_id.id if next_id else None
    }
    params.update(generate_view_params(request))
    return render(request, 'app/one_ad.html', params)


def all_ads(request):
    paginator = Paginator(Ad.objects.filter(is_active=True).order_by('-updated_at'), 12)
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
    form = AdCreationForm(request.POST, files=request.FILES)
    if request.POST:
        if form.is_valid():
            new_ad = Ad()
            new_ad.title = form.cleaned_data['title']
            new_ad.description = form.cleaned_data['description']
            new_ad.category = form.cleaned_data['category']
            new_ad.city = form.cleaned_data['city']
            new_ad.metro = form.cleaned_data['metro']
            new_ad.phone = form.cleaned_data['phone']
            new_ad.user = request.user if request.user and not request.user.is_anonymous else None
            new_ad.price = form.cleaned_data['price'] if form.cleaned_data['price'] else 'Договорная'
            temp_location = json.loads(form.cleaned_data['location'])
            location = Coordinates()
            position = Geoposition(temp_location['lat'], temp_location['lng'])
            location.position = position
            location.save()
            new_ad.location = location
            new_ad.is_active = False
            new_ad.save()
            for f in request.FILES.getlist('images'):
                media = Media()
                media.media_file = f
                media.save()
                new_ad.media.add(media)

            link_to_ad = SITE_PROTOCOL + SITE_URL + '/admin/ad_app/ad/' + str(new_ad.id) + '/change'
            message = '<b>Пользователь:</b>' + str(new_ad.user) if new_ad.user else 'Аноним'
            message += '<br>' + '<b>Дата:</b>' + str(datetime.date.today()) + '<br>' + '<b>Ссылка:</b> <a href="' + link_to_ad + '" target="_blank">' + link_to_ad + '</a>'
            thread = threading.Thread(target=send_email_notification, args=('Новое объявление',
                                                                            mark_safe(message),
                                                                            ADMIN_EMAIL))
            thread.start()
            return HttpResponseRedirect(reverse('ad:one_ad', kwargs={'ad_id': new_ad.id}))
        else:
            print form.errors
            return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('index'))


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        filters = dict()
        if form.cleaned_data['search_word']:
            filters['title__icontains'] = form.cleaned_data['search_word'].lower().strip()
        if form.cleaned_data['categories']:
            category = Category.objects.filter(id=int(form.cleaned_data['categories'])).first()
            if not category.parent:
                children = Category.objects.filter(parent=category)
                ids = [category.id]
                for item in children:
                    ids.append(item.id)
                filters['category__id__in'] = ids
            else:
                filters['category'] = category

        if form.cleaned_data['metro']:
            metro = Metro.objects.filter(id=int(form.cleaned_data['metro'])).first()
            filters['metro'] = metro

        if form.cleaned_data['city']:
            city = City.objects.filter(id=int(form.cleaned_data['city'])).first()
            filters['city'] = city

        filters['is_active'] = True
        paginator = Paginator(Ad.objects.filter(**filters).order_by('-updated_at'), 12)
        ads = paginator.page(request.GET.get('page', 1))
        params = {
            'ads': ads,
            'pagination': ads
        }
        params.update(generate_view_params(request))
        return render(request, 'app/all_ads.html', params)
    else:
        return render(request, 'app/all_ads.html', generate_view_params(request))


def send_email_notification(title, body, to):
    email = EmailMessage(title, body=body, to=to)
    email.content_subtype = 'html'
    email.send()

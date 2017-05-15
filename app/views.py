# coding=utf-8
import random

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from categories.views import get_categories, generate_view_params
from categories.models import Category
from ad_app.models import Ad, Media
from users_app.models import Users
from Classified.settings import STATIC_ROOT
from .models import Metro, City, AboutUs
from posts_app.models import Post


# Create your views here.


def index(request):
    ads = Ad.objects.filter(is_active=True)[:12]
    posts = Post.objects.all()
    params = {
        'ads': ads,
        'posts': posts
    }
    params.update(generate_view_params(request))
    return render(request, 'app/index.html', params)


def about(request):
    content = AboutUs.objects.first()
    params = {
        'content': content
    }
    params.update(generate_view_params(request))
    return render(request, 'app/about_us.html', params)


def fixtures(request, thread):
    if thread == 'ads':
        images = list()
        city = City()
        city.title = u'Москва'
        city.save()
        metro = Metro()
        metro.title = u'Пушкино'
        metro.save()
        thumbnails = [
            'good-1.png',
            'good-2.png',
            'good-3.png'
        ]
        for j in range(0, 2):
            image = Media()
            image.media_file.file = STATIC_ROOT + '/images/' + thumbnails[j]
            image.save()
            images.append(image)
        for i in range(0, 50):
            item = Ad()
            item.title = u'Test title ' + str(random.randrange(1000, 9999))
            item.description = u'Lorem ipsum dolor sit amet'
            item.metro = metro
            item.city = city
            item.category = Category.objects.filter(parent=None).first()
            item.phone = u'+996 707 330 726'
            item.user = Users.objects.filter().first()
            item.price = 15000
            item.save()
            for image in Media.objects.all():
                item.media.add(image)
        return JsonResponse(dict(success=True))
    if thread == 'categories':
        pass
    return JsonResponse(dict(success=False, messages='No thread are selected'))


def get_metro_by_city(request):
    city = request.POST.get('city')
    metros = Metro.objects.filter(city=City.objects.get(id=city))
    choices = ['<option value>Метро</value>']
    for item in metros:
        choices.append('<option value="' + str(item.id) + '" style="color: #' + item.color + ';">' + item.title + '</option>')

    return HttpResponse(choices)

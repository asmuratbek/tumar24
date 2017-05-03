# coding=utf-8
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from ad_app.models import Ad
# from app.views import generate_view_params

# Create your views here.


def generate_view_params(request):
    params = {
        'categories': get_categories()
    }
    return params


def get_categories():
    categories = list()
    parent_categories = Category.objects.filter(parent=None).all()
    for item in parent_categories:
        child_categories = Category.objects.filter(parent=item).all()
        categories.append({'parent': item, 'child': child_categories})

    return categories


def parent_category(request, category):
    cat = Category.objects.filter(slug=category).first()
    pagination = Paginator(Ad.objects.filter(category=cat), 12)
    ads = pagination.page(request.GET.get('page', 1))
    params = {
        'category': cat,
        'ads': ads,
        'pagination': ads
    }
    params.update(generate_view_params(request))
    return render(request, 'app/category.html', params)


def child_category(request, category, child):
    cat = Category.objects.filter(slug=child, parent__slug=category).first()
    pagination = Paginator(Ad.objects.filter(category=cat), 12)
    ads = pagination.page(request.GET.get('page', 1))
    params = {
        'category': cat,
        'ads': ads,
        'pagination': ads
    }
    params.update(generate_view_params(request))
    print params
    return render(request, 'app/category.html', params)

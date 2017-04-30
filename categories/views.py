# coding=utf-8
from django.shortcuts import render
from .models import *
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
    params = {
        'category': cat
    }
    params.update(generate_view_params(request))
    return render(request, 'app/category.html', params)


def child_category(request, category):
    cat = Category.objects.filter(slug=category).first()
    parent = cat.parent_category
    params = {
        'category': cat,
        'parent_category': parent
    }
    params.update(generate_view_params(request))
    return render(request, 'app/category.html', params)

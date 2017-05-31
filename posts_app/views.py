from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from .models import *
from categories.views import generate_view_params
from django.core.exceptions import ObjectDoesNotExist
from Classified.parameters import SITE_PROTOCOL, SITE_URL
from django.http import Http404

# Create your views here.


def all_posts(request):
    paginator = Paginator(Post.objects.all().order_by('-updated_at'), 10)
    posts = paginator.page(request.GET.get('page', 1))

    params = {
        'posts': posts,
        'pagination': posts,
    }
    params.update(generate_view_params(request))
    return render(request, 'app/all_posts.html', params)


def one_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except ObjectDoesNotExist:
        raise Http404

    hit_count = HitCount.objects.get_for_object(post)
    response = HitCountMixin.hit_count(request, hit_count)
    if response.hit_counted:
        post.views += 1
        post.save()

    prev_id = Post.objects.filter(id__lt=post_id).last()
    next_id = Post.objects.filter(id__gt=post_id).first()

    absolute_path = SITE_PROTOCOL + SITE_URL + reverse('news:one_post', kwargs={'post_id': post_id})

    params = {
        'post': post,
        'prev': prev_id,
        'next': next_id,
        'absolute_path': absolute_path
    }
    params.update(generate_view_params(request))
    return render(request, 'app/one_post.html', params)

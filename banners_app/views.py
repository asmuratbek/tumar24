import random

from django.shortcuts import render
from .models import VerticalBanners, HorizontalBanners


# Create your views here.


def get_vertical_banner_by_ratio():
    ids = []
    for item in VerticalBanners.objects.filter(is_active=True):
        ids.append(item.id)

    result = []
    if len(ids) > 1:
        second_id = first_id = random.randint(ids[0], ids[len(ids) - 1])
        result.append(VerticalBanners.objects.get(id=first_id))
        while second_id == first_id:
            second_id = random.randint(ids[0], ids[len(ids) - 1])

        if second_id != first_id:
            result.append(VerticalBanners.objects.get(id=second_id))

    return result


def get_horizontal_banner():
    if HorizontalBanners.objects.count() > 0:
        random_index = random.randint(0, HorizontalBanners.objects.count() - 1)
        return HorizontalBanners.objects.all()[random_index]
    else:
        return None



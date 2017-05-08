# coding=utf-8
from django import template

register = template.Library()


@register.filter
def make_translit(value):
    print value.replace(' ', '-')
    return value.replace(' ', '-')

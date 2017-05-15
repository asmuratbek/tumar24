# coding=utf-8
from django import template

register = template.Library()


@register.filter
def make_translit(value):
    print value.replace(' ', '-')
    return value.replace(' ', '-')


@register.filter
def render_boolean(value):
    if value:
        return u'<span style="color: green;">Активный</span>'
    return u'<span style="color: red;">Неактивный</span>'

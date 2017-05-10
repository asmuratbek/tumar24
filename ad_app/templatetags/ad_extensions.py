from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def array_slice(array, start, step=None):
    return array[start:start+(step if step else 0)]


@register.filter
def array_slice_filter(array, start):
    if len(array) > 10:
        return array[start-1:start+5]
    return array


@register.filter
def div(value, param):
    return value / param


@register.filter
def plus(a, b):
    return a + b

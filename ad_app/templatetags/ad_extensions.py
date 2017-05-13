# coding=utf-8
from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def array_slice(array, start, step=None):
    return array[start:start + (step if step else 0)]


@register.filter
def array_slice_filter(array, start):
    if len(array) > 10:
        return array[start - 1:start + 5]
    return array


@register.filter
def div(value, param):
    return value / param


@register.filter
def plus(a, b):
    return int(a) + int(b)


@register.filter
def minus(a, b):
    return int(a) - int(b)


@register.simple_tag
def show_link(page, num_pages, current_page):
    page = int(page)
    num_pages = int(num_pages)
    current_page = int(current_page)

    if page == current_page:
        return True
    if (page <= 5 and current_page <= 5) or (page >= num_pages - 5 and current_page >= num_pages - 5):
        return True

    if page == 1 or page == num_pages:
        return True

    if current_page - page in [1, 2] or page - current_page in [1, 2]:
        return True

    return False


@register.assignment_tag
def set(value):
    return value


@register.filter
def clear_spaces(value):
    new_text = value.replace(u"&nbsp;", u" ")\
        .replace('<p>', '')\
        .replace('</p>', '')\
        .replace('<pre>', '')\
        .replace('</pre>', '')
    return new_text

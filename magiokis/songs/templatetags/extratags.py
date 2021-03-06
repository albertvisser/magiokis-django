"""Custom tags for Magiokis Songs Django version
"""
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


# @register.filter
# @stringfilter
# def nbrk(value):
#     "Make all spaces nonbreaking"
#     return value.replace(' ', '&nbsp;')
# nbrk.is_safe = True


@register.filter
@stringfilter
def nbrk(value, autoescape=None):
    "Make all spaces nonbreaking"
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(esc(value.replace(' ', '&nbsp;')))
nbrk.needs_autoescape = False
nbrk.is_safe = True


# def initial_letter_filter(text, autoescape=None):
#     first, other = text[0], text[1:]
#     if autoescape:
#         esc = conditional_escape
#     else:
#         esc = lambda x: x
#     result = '<strong>%s</strong>%s' % (esc(first), esc(other))
#     return mark_safe(result)
# initial_letter_filter.needs_autoescape = True

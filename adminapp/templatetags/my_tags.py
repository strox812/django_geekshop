from django.conf import settings
from django import template


register = template.Library()

@register.filter(name='media_for_products')
def media_for_products(path_to_image):
    if not path_to_image:
        return '{settings.STATIC_URL}img/default.jpg'

    return f'{settings.MEDIA_URL}{path_to_image}'

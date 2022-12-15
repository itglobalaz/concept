from django.template import Library

from src.configuration.models import Config, Seo, Social
from src.main.models import Slider, Services

register = Library()


@register.simple_tag()
def get_config():
    return Config.objects.get()


@register.simple_tag()
def get_seo():
    return Seo.objects.get()


@register.simple_tag()
def get_social():
    return Social.objects.order_by('id')


@register.simple_tag()
def get_slider():
    return Slider.objects.order_by('id')[:3]


@register.simple_tag()
def get_services():
    return Services.objects.order_by('id')

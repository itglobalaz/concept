from django.template import Library

from src.configuration.models import Config, Seo, Social

register = Library()


@register.simple_tag()
def get_config():
    return Config.objects.get()


@register.simple_tag()
def get_seo():
    return Seo.objects.get()


@register.simple_tag()
def get_social():
    return Social.objects.order_by('-id')

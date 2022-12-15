from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.configuration.models import Seo, Config


class ConfigTranslationOptions(TabbedTranslationAdmin):
    list_display = ('phone',)
    required_languages = ('az',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Config, ConfigTranslationOptions)


class SeoTranslationOptions(TabbedTranslationAdmin):
    list_display = ('title', 'description', 'keywords')
    required_languages = ('az',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Seo, SeoTranslationOptions)
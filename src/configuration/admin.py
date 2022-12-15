from django.contrib import admin

from src.configuration.models import Seo, Social, Config
from modeltranslation.translator import TranslationOptions, translator

admin.site.site_header = "Concept House idarəetmə paneli"
admin.site.site_title = "Xoş gəldiniz İlqar!"
admin.site.index_title = 'Xoş gəldiniz İlqar!'


class ConfigTranslationOption(TranslationOptions):
    fields = ('address',)
    required_languages = ('az',)


translator.register(Config, ConfigTranslationOption)


class SeoTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'keywords')
    required_languages = ('az',)


translator.register(Seo, SeoTranslationOption)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name',)

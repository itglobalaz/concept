from django.contrib import admin
from modeltranslation.translator import translator, TranslationOptions
from src.main.models import Slider, About, Services, WhyUs, WhyUsReason, Team, Testimonials
from django_summernote.models import Attachment

admin.site.unregister(Attachment)


class SliderTranslationOption(TranslationOptions):
    fields = ('title', 'subtitle',)


translator.register(Slider, SliderTranslationOption)


class AboutTranslationOption(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = ('az',)


translator.register(About, AboutTranslationOption)


class ServiceTranslationOption(TranslationOptions):
    fields = ('name', 'description', 'keywords')
    required_languages = ('az',)


translator.register(Services, ServiceTranslationOption)


class WhyUsTranslationOption(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('az',)


translator.register(WhyUs, WhyUsTranslationOption)


class WhyUsReasonTranslationOption(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('az',)


translator.register(WhyUsReason, WhyUsReasonTranslationOption)


class TeamTranslationOption(TranslationOptions):
    fields = ('full_name', 'position')
    required_languages = ('az',)


translator.register(Team, TeamTranslationOption)


class TestimonialsTranslationOption(TranslationOptions):
    fields = ('full_name', 'description',)
    required_languages = ('az',)


translator.register(Testimonials, TestimonialsTranslationOption)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from src.main.models import Slider, About, Services, WhyUsReason, WhyUs, Team, Testimonials, Project, ProjectPhoto


class SliderTranslationOptions(TabbedTranslationAdmin):
    list_display = ('title', 'image', 'get_image',)
    list_editable = ('image',)
    ordering = ['id']


admin.site.register(Slider, SliderTranslationOptions)


class AboutTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    required_languages = ('az',)
    summernote_fields = ('description',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(About, AboutTranslationOptions)


class ServiceTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('name', 'service_icon',)
    list_editable = ('service_icon',)
    required_languages = ('az',)
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Services, ServiceTranslationOptions)


class ReasonInline(TranslationTabularInline):
    model = WhyUsReason
    extra = 1

    verbose_name = "Səbəb"
    verbose_name_plural = "Səbəb"


class WhyUsTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    required_languages = ('az',)
    summernote_fields = ('description',)
    inlines = [ReasonInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(WhyUs, WhyUsTranslationOptions)


class TeamTranslationOptions(TabbedTranslationAdmin):
    list_display = ('full_name',)


admin.site.register(Team, TeamTranslationOptions)


class TestimonialTranslationOptions(TabbedTranslationAdmin):
    list_display = ('full_name',)


admin.site.register(Testimonials, TestimonialTranslationOptions)


class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    extra = 1


class ProjectTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('name',)
    prepopulated_fields = ({'slug': ('name',)})
    summernote_fields = ('description',)
    inlines = [ProjectPhotoInline]


admin.site.register(Project, ProjectTranslationOptions)

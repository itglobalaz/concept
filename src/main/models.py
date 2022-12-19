from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/', verbose_name='Şəkil')
    title = models.TextField(max_length=255, verbose_name='Başlıq')
    subtitle = models.TextField(max_length=255, verbose_name='Alt başlıq', blank=True)

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = '1. Slayderlər'

    def __str__(self):
        return self.title

    def get_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    get_image.short_description = 'Şəkil'


class About(models.Model):
    photo = models.ImageField(upload_to='about/', verbose_name='Şəkil')
    photo_two = models.ImageField(upload_to='about/', verbose_name='Şəkil 2')
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Məlumat")
    counter = models.PositiveIntegerField(verbose_name="İl iş təcrübəsi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "2. Haqqımızda"


class Services(models.Model):
    service_photo = models.ImageField(upload_to='services_photo/', null=True, blank=True, verbose_name='Şəkil')
    service_icon = models.ImageField(upload_to='services_icons/', null=True, blank=True, verbose_name='Ikon')
    name = models.CharField(max_length=255, blank=False, verbose_name="Başlıq")
    description = models.TextField(max_length=5000, verbose_name="Məlumat")
    keywords = models.CharField(max_length=255, verbose_name='Açar sözlər', blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = '3. Xidmətlər'

    def get_service_url(self):
        return reverse('service_detail', args=[self.slug])

    def __str__(self):
        return self.name


class WhyUs(models.Model):
    photo = models.ImageField(upload_to='about/', verbose_name='Şəkil')
    photo_two = models.ImageField(upload_to='about/', verbose_name='Şəkil 2')
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Məlumat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Niyə biz?"
        verbose_name_plural = "4. Niyə biz?"


class WhyUsReason(models.Model):
    chooice = models.ForeignKey(WhyUs, verbose_name="Seçim", on_delete=models.CASCADE, related_name="labels")
    icon = models.ImageField(upload_to='whyus/', verbose_name='İkon')
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.CharField(max_length=255, blank=True, verbose_name='Məlumat')

    def __str__(self):
        return self.title


class Team(models.Model):
    photo = models.ImageField(upload_to='team/', verbose_name="Şəkil")
    full_name = models.CharField(max_length=255, verbose_name="Ad Soyad")
    position = models.CharField(max_length=255, verbose_name="Vəzifə")
    facebook = models.URLField(verbose_name='Facebook', blank=True)
    instagram = models.URLField(verbose_name='Instagram', blank=True)
    whatsapp = models.CharField(max_length=255, help_text='Misal: +994504996588', verbose_name='Whatsapp', blank=True)

    class Meta:
        verbose_name = 'Komanda'
        verbose_name_plural = '5. Komandamız'

    def __str__(self):
        return self.full_name


class Testimonials(models.Model):
    photo = models.ImageField(upload_to='team/', blank=True, verbose_name="Şəkil")
    full_name = models.CharField(max_length=255, verbose_name="Ad Soyad")
    description = models.TextField(max_length=255, verbose_name="Rəy")

    class Meta:
        verbose_name = 'Rəy'
        verbose_name_plural = '6. Rəylər'

    def __str__(self):
        return self.full_name


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad")
    description = models.TextField(verbose_name='Məlumat')
    start_date = models.DateField(verbose_name="Tarix")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Xidmət")
    style = models.CharField(max_length=255, verbose_name="Stil")
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Layihə'
        verbose_name_plural = '7 Layihələr'

    def __str__(self):
        return self.name

    def get_project_url(self):
        return reverse('project_detail', args=[self.slug])


class ProjectPhoto(models.Model):
    chooice = models.ForeignKey(Project, verbose_name='Layihə', on_delete=models.CASCADE, related_name='project_photo')
    photo = models.ImageField(upload_to='projects/', verbose_name='Şəkil')

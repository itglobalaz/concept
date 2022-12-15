from django.db import models


class Config(models.Model):
    logo = models.ImageField(upload_to='siteLogo/', verbose_name='Loqo')
    phone = models.CharField(max_length=255, verbose_name="Əlaqə")
    email = models.EmailField(verbose_name="Poçt")
    address = models.CharField(max_length=255, verbose_name="Ünvan")
    map = models.CharField(max_length=1000, verbose_name="Xəritə link", null=True)

    class Meta:
        verbose_name = "Ayarlar"
        verbose_name_plural = "1. Əlaqə & Loqo"

    def __str__(self):
        return self.phone


class Seo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlıq')
    description = models.TextField(verbose_name="Məlumat")
    keywords = models.TextField(max_length=255, verbose_name="Açar sözlər",
                                help_text="Misal: Saytların hazırlanması, dizayn işləri")

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "2. SEO"

    def __str__(self):
        return self.title


class Social(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad", help_text="fb, tw, ins")
    url = models.CharField(max_length=255, verbose_name="URL", help_text="facebook.com, +994504996588")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sosial şəbəkə"
        verbose_name_plural = "3. Sosial şəbəkə"

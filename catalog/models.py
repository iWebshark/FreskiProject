from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=250, verbose_name='Описание', blank=False, null=False)
    provider_link = models.CharField(max_length=250, blank=True, null=True, verbose_name='Ссылка на поставщика')

    def __str__(self):
        return self.name


class FrescoProvider(Provider):
    provider_img = models.ImageField(upload_to='catalog/fresco', blank=True, null=True, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Фрески'
        verbose_name_plural = 'Фрески'


class FretworkProvider(Provider):
    provider_img = models.ImageField(upload_to='catalog/fretwork', blank=True, null=True, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Лепнина'
        verbose_name_plural = 'Лепнина'


class GlueProvider(Provider):
    provider_img = models.ImageField(upload_to='catalog/glue', blank=True, null=True, verbose_name='Фото товара')
    price = models.CharField(max_length=150, verbose_name='Цена', null=False, blank=False)

    provider_country = models.CharField(max_length=250, verbose_name='Страна производитель', null=True, blank=True)
    rate = models.CharField(max_length=250, verbose_name='Расход', null=True, blank=True)

    class Meta:
        verbose_name = 'Клей'
        verbose_name_plural = 'Клей'

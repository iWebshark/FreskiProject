from django.db import models


# Examples with Images
class Example(models.Model):
    name = models.CharField(max_length=250, verbose_name='Описание')
    producer = models.CharField(max_length=250, blank=True, null=True, verbose_name='Производитель')
    default_image = models.ImageField(upload_to='examples/', blank=True, null=True, verbose_name='Основная картика')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'


class ExampleImage(models.Model):
    example = models.ForeignKey(Example, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='examples/', verbose_name='Картинка')

    def __str__(self):
        return self.example.name

    class Meta:
        verbose_name = 'Пример (картинка)'
        verbose_name_plural = 'Галерея проекта'


# Contacts
class Contact(models.Model):

    CONTACT_CHOICES = (
        ('Адрес', 'Адрес'),
        ('Телефон', 'Телефон'),
        ('Email', 'Email'),
        ('Расписание', 'Расписание')
    )

    tag = models.CharField(max_length=15, unique=True, verbose_name='Тип',
                           choices=CONTACT_CHOICES, default='Адрес')
    value = models.CharField(max_length=250, unique=True, verbose_name='Значение')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

# Generated by Django 3.1.6 on 2021-04-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210423_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tag',
            field=models.CharField(choices=[('Адрес', 'Адрес'), ('Телефон', 'Телефон'), ('Email', 'Email'), ('Расписание', 'Расписание')], default='Адрес', max_length=15, unique=True, verbose_name='Тип'),
        ),
    ]

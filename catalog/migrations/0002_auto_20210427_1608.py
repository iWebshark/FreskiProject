# Generated by Django 3.1.6 on 2021-04-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='provider_img',
        ),
        migrations.AddField(
            model_name='frescoprovider',
            name='provider_img',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/fresco', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='fretworkprovider',
            name='provider_img',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/fretwork', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='glueprovider',
            name='provider_img',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/glue', verbose_name='Фото товара'),
        ),
    ]

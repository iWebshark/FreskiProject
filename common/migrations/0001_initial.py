# Generated by Django 3.1.6 on 2021-04-23 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('Адрес', 'Адрес'), ('Телефон', 'Телефон'), ('Email', 'Email')], default='Адрес', max_length=10, unique=True, verbose_name='Тип')),
                ('value', models.CharField(max_length=250, unique=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Описание')),
                ('producer', models.CharField(blank=True, max_length=250, null=True, verbose_name='Производитель')),
                ('default_image', models.ImageField(blank=True, null=True, upload_to='examples/', verbose_name='Основная картика')),
            ],
            options={
                'verbose_name': 'Пример работы',
                'verbose_name_plural': 'Примеры работ',
            },
        ),
        migrations.CreateModel(
            name='ExampleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='examples/', verbose_name='Картинка')),
                ('example', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='common.example')),
            ],
            options={
                'verbose_name': 'Пример (картинка)',
                'verbose_name_plural': 'Галерея проекта',
            },
        ),
    ]

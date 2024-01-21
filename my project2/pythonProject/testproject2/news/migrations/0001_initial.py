# Generated by Django 5.0.1 on 2024-01-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titl', models.CharField(default='Новость', max_length=50, verbose_name='Название')),
                ('anonse', models.CharField(max_length=60, verbose_name='Анонс новости')),
                ('full_txt', models.TextField(verbose_name='Содержание')),
                ('date_time', models.DateTimeField(verbose_name='Дата и время выпуска статьи')),
            ],
        ),
    ]

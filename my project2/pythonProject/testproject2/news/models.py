from django.db import models

class Articles(models.Model):
    titl = models.CharField('Название', max_length=50, default="Новость")
    anonse = models.CharField("Анонс новости", max_length=60)
    full_txt = models.TextField("Содержание")
    date_time = models.DateTimeField("Дата и время выпуска статьи")


    def __str__(self):
        return f'Новость {self.titl}'

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
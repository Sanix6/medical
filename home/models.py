from django.db import models


class Slider(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    subtitle = models.CharField('Подзоголовок', max_length=255, null=True, blank=True)
    img = models.ImageField('Изоброжение', null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)
    is_activate = models.BooleanField('Активность', default=False)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Direction(models.Model):
    image = models.ImageField('Изоброжение', null=True, blank=True)
    title = models.CharField('Направление',max_length=55, null=True, blank=True)

    class Meta:
        verbose_name = 'Направление Института'
        verbose_name_plural = 'Направление Института'


class Gallery(models.Model):
    image = models.ImageField('Изоброжение', null=True, blank=True)
    year = models.IntegerField(
        default=2010,
        choices=[(year, year) for year in range(2010, 2041)],
        verbose_name="Год фотографии",
    )

    def __str__(self):
        return f'{self.year}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерии'


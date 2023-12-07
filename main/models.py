from django.db import models
from django.db.models import CASCADE


class Doctor(models.Model):
    image = models.ImageField('Изоброжение', null=True, blank=True)
    full_name = models.CharField('Фио', max_length=55, null=True, blank=True)
    direction = models.CharField('Направление врача', max_length=255, null=True, blank=True)
    experience = models.CharField('Опыт работы', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'О Медике'
        verbose_name_plural = 'O Медике'


class Cont(models.Model):
    cat = models.ForeignKey(Doctor, on_delete=CASCADE, related_name='cat')
    number = models.IntegerField('Номер телефона', null=True, blank=True)


class News(models.Model):
    image = models.ImageField('Изоброжение', null=True, blank=True)
    title = models.CharField('Название статьи', max_length=255, null=True, blank=True)
    subtitle = models.TextField('Статья', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

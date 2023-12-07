from django.db import models
from solo.models import SingletonModel


class Contact(SingletonModel):
    numbers = models.IntegerField('Номер телефона', null=True, blank=True)
    location = models.CharField('Местоположение', max_length=55, null=True, blank=True)
    email = models.EmailField('Электронный адрес', null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

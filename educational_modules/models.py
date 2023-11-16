from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Module(models.Model):
    """Класс для отображения образовательных модулей"""
    numbers = models.PositiveSmallIntegerField(verbose_name='Порядковый номер', **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='название образовательного модуля')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'образовательный модуль'
        verbose_name_plural = 'образовательные модули'

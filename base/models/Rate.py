from django.db import models


class Rate(models.Model):
    name = models.CharField(max_length=100)
    count_restaurants = models.PositiveSmallIntegerField('Количество ресторанов', default=1,)
    count_menu = models.PositiveSmallIntegerField('Количество меню', default=5,)
    count_menu_items = models.PositiveSmallIntegerField('Количество позиций в меню', default=15,)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name

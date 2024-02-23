from django.db import models
from base.models.Base import Base
from base.models.Restaurant import Restaurant
class Category(Base):
    restaurant_ref = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = 'categories')
    name = models.CharField(max_length = 255)
    descriptions = models.CharField('Описание', max_length = 255, blank = True, null=True)

    def __str__(self):
        return self.name
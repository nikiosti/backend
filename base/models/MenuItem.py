from django.db import models
from base.models.Base import Base
from base.models.Category import Category


import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

import random

def get_default_image():
    return random.choice([
        '/noimage_edaded_placeholder_1.png',
        '/noimage_edaded_placeholder_2.png',
        '/noimage_edaded_placeholder_3.png',
        '/noimage_edaded_placeholder_4.png',
        '/noimage_edaded_placeholder_5.png',
        '/noimage_edaded_placeholder_6.png',
        '/noimage_edaded_placeholder_7.png',
    ])


class MenuItem(Base):
    category_ref = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'items')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight_in_grams = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField('Картика', upload_to='menu_item/', blank=True, null=True, default=get_default_image)

    def __str__(self):
        return self.name
    

class MenuItemPrice(Base):
    menu_item_ref = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='prices')
    size_description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

@receiver(pre_delete, sender=MenuItem)
def menuitem_pre_delete(sender, instance, **kwargs):
 
    if instance.image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
        if os.path.exists(image_path):
            os.remove(image_path)

@receiver(pre_save, sender=MenuItem)
def menuitem_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = MenuItem.objects.get(pk=instance.pk)
            old_image = old_instance.image if old_instance else None
            new_image = instance.image if instance.image else None
            if old_image != new_image:
                if old_image:
                    old_image_path = os.path.join(settings.MEDIA_ROOT, str(old_image))
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
        except MenuItem.DoesNotExist:
            pass  


pre_delete.connect(menuitem_pre_delete, sender=MenuItem)
pre_save.connect(menuitem_pre_save, sender=MenuItem)
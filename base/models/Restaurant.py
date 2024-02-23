from django.db import models
from base.models.Base import Base

import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

class Restaurant(Base):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField('Картика',upload_to='restaurants/', blank=True, null=True)
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    is_visible = models.BooleanField('Видемость', default=True)
    working_hours = models.CharField('Время работы', max_length = 255, blank=True, null=True)
    wifi_password = models.CharField('wifi', max_length = 255, blank=True, null=True)


    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):      
        return self.name
    


@receiver(pre_delete, sender=Restaurant)
def restaurant_pre_delete(sender, instance, **kwargs):
 
    if instance.image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
        if os.path.exists(image_path):
            os.remove(image_path)


@receiver(pre_save, sender=Restaurant)
def restaurant_pre_save(sender, instance, **kwargs):
  
    if instance.pk:
        try:
            old_instance = Restaurant.objects.get(pk=instance.pk)
            old_image = old_instance.image if old_instance else None
            new_image = instance.image if instance.image else None

            if old_image != new_image:
         
                if old_image:
                    old_image_path = os.path.join(settings.MEDIA_ROOT, str(old_image))
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
        except Restaurant.DoesNotExist:
            pass  


pre_save.connect(restaurant_pre_save, sender=Restaurant)
pre_delete.connect(restaurant_pre_delete, sender=Restaurant)
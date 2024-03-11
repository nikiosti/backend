from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Restaurateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    phoneOrMessenger = models.CharField(max_length=255, null=True)

    job_title = models.CharField(max_length=255)
    rate = models.ForeignKey("base.Rate", on_delete=models.SET_NULL, null=True)
    is_visible_restaurants = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Ресторатор"
        verbose_name_plural = "Рестораторы"

    def __str__(self):
        return self.user.username


class RestaurateurFormInLendingPage(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneOrMessenger = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

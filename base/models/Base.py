from django.db import models
import uuid


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        "base.Restaurateur", on_delete=models.CASCADE, verbose_name="Ресторатор"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

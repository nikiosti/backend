# Generated by Django 5.0 on 2024-02-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_menuitemprice_id_menuitemprice_base_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

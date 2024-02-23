# Generated by Django 5.0 on 2024-01-02 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_category_restaurant_ref_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_item/', verbose_name='Картика'),
        ),
        migrations.AlterField(
            model_name='category',
            name='restaurant_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='base.restaurant'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='base.category'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-11-14 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0002_auto_20230204_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='comic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic', verbose_name='comic'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

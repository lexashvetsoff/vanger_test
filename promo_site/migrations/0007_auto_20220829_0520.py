# Generated by Django 2.2 on 2022-08-29 05:20

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('promo_site', '0006_slider_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='bg_image',
            field=filer.fields.image.FilerImageField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='bg', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение'),
        ),
    ]
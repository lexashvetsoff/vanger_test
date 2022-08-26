from email.policy import default
from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField

class Slider(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название слайдера'
    )

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    slider = models.ForeignKey(
        Slider,
        verbose_name='Слайдер',
        on_delete=models.CASCADE,
        related_name='images'
    )
    order_number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
        default=0
    )
    image = FilerImageField(
        verbose_name='Изображение',
        on_delete=models.CASCADE,
        related_name='slider_images',
    )

    class Meta:
        ordering = ['order_number']

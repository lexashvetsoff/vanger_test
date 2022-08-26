from django.shortcuts import render
from django.urls import reverse

from promo_site.models import Slider, SliderImage


def index(request):
    print(reverse('show_promo'))
    context = {
        'url': reverse('show_promo'),
        'url_admin': '/admin',
    }
    return render(request, 'index.html', context)


def show_promo(request):
    slider = Slider.objects.all()[0]
    slider_imgs = SliderImage.objects.all().filter(slider=slider)
    
    imgs = [img.image.url for img in slider_imgs]

    context = {
        'imgs': imgs
    }
    return render(request, 'promo.html', context)

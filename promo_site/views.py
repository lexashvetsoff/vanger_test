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
    all_sliders = []
    sliders = Slider.objects.all()

    for slider in sliders:
        slider_imgs = SliderImage.objects.all().filter(slider=slider)
        imgs = [img.image.url for img in slider_imgs]
        slider_id = '{}_{}'.format(slider.name, slider.id)
        nav_slider_id = 'nav_{}_{}'.format(slider.name, slider.id)
        if slider.bg_image:
            # bg_image = slider.bg_image.url
            bg_image = 'url("{}")'.format(slider.bg_image.url)
        else:
            bg_image = '#507D2A'
        data_sliders = {
            'title': slider.title,
            'bg_image': bg_image,
            'slider_id': slider_id,
            'nav_slider_id': nav_slider_id,
            'images': imgs
        }
        print(bg_image)
        all_sliders.append(data_sliders)

    context = {
        'all_sliders': all_sliders
    }
    return render(request, 'promo.html', context)

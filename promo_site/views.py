from django.shortcuts import render
from django.urls import reverse


def index(request):
    print(reverse('show_promo'))
    context = {
        'url' : reverse('show_promo')
    }
    return render(request, 'index.html', context)


def show_promo(request):
    context = {}
    return render(request, 'promo.html', context)

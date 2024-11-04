from django.shortcuts import render
from categorygame.models import *


def category(request, category_slug):

    category = Category.objects.get(slug=category_slug)

    buldy = Buld.objects.filter(category__slug=category_slug)
    
    context = {
        'buldy': buldy,
        'category': category,
            
    }
    
    return render(request, 'category.html', context)

def buld(request, category_slug, buld_slug):

    category = Category.objects.get(slug=category_slug)

    buldys = Buld.objects.get(category__slug=category_slug, slug=buld_slug)

    context = {
        'title': 'BuldMMO | |',
        'buldys': buldys,
        'category': category,
    }

    return render(request, 'buld.html', context)


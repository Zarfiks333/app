from django.http import HttpResponse
from django.shortcuts import render

from categorygame.models import *

def index(request):
   
    context = {
      'title': 'BuldMMO',
    }

    return render(request, 'index.html', context)

def newbuld(request):
    context = {
        'title': 'BuldMMO | Свежие билды',
    }
    return render(request, 'newbuld.html', context)

def new(request):
    context = {
        'title': 'BuldMMO | Новости',
    }
    return render(request, 'new.html', context)

def forum(request):
    context = {
        'title': 'BuldMMO | Форум',
        'content': 'В разработке...',
    }
    return render(request, 'forum.html', context)

def rmtgame(request):
    context = {
        'title': 'BuldMMO | Рмт информация',
    }
    return render(request, 'rmtgame.html', context)



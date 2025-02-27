from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html')


def notes(request):
    topic_list = Topics.objects.all()
    context = {'topic_list': topic_list}
    return render(request, 'notes.html', context)


def pastpaper(request):
    pastpaper_list = PastPaper.objects.all()
    sibal = ['2024 Mar', '2023 Nov', '2023 May', '2023 Mar', '2022 Nov', '2022 May', '2022 Mar', '2021 Nov', '2021 May', '2021 Mar', '2020 Nov', '2020 May', '2020 Mar']
    context = {'pastpaper_list': pastpaper_list, 'sibal': sibal}
    return render(request, 'pastpaper.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')


def examtips(request):
    return render(request, 'examtips.html')

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Page my_app")


def page_1(request):
    return HttpResponse("Page 1")


def page_2(request):
    return HttpResponse("Page 2")

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Main page my_app")


# def page_1(request):
#     return HttpResponse("Page 1")


# def page_2(request):
#     return HttpResponse("Page 2")


def products(request, number_product):
    if number_product == 1:
        return HttpResponse("Product 1. Product description...")
    elif number_product == 2:
        return HttpResponse("Product 2. Product description...")
    else:
        return HttpResponseNotFound(f'Error 404! Product {number_product} not found.')


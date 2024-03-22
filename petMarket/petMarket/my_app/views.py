from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Main page my_app")


def products(request, number_product):
    if number_product == 1:
        return render(request, 'page_1.html')
    elif number_product == 2:
        return HttpResponse("Product 2. Product description...")
    else:
        return render(request, "pageNotFound404.html", status=404)


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Main page my_app")


def products(request, number_product):
    data = {
        'number_product': number_product,
        'info_page': None,
    }
    if number_product in [1, 2]:
        data['info_page'] = f'Product information {number_product}...'
        return render(request, 'page_1.html', context=data)
    else:
        return render(request, "pageNotFound404.html", status=404)

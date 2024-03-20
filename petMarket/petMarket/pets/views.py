from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная Кошки Собаки")


# def cats(request):
#     return HttpResponse("<h2>Кошки<h2>")


# def dogs(request):
#     return HttpResponse("<h2>Собаки<h2>")


def categories(request, category_id):
    return HttpResponse(f"Категории: id={category_id}")


def pet(request, pet_slug):
    if pet_slug in ['cats', 'dogs']:
        return HttpResponse(pet_slug)
    return HttpResponseNotFound('Error 404!')


def petGET(request):
    title = request.GET.get('title')
    return HttpResponse(f'Title: {title}')


from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


class Cat:
    def __init__(self):
        self.name = "Cat"
        self.age = 3

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


def pet(request, pet_slug):
    data = {
        "pet_name": pet_slug,
        "pet_text": "Это текст про страницу с животными",
        "pet_list": ["Кот", "Собака"],
        "pet_int": 34,
        "pet_dict": {"cat": "Кот", "dog": "Собака"},
        "pet_obj": Cat()
    }

    # будем делать обращение к БД "существует ли pet_slug?"
    if pet_slug in ['cats', 'dogs']:
        return render(request, "pet_page.html", context=data)  # context преобразует все к строке
    return render(request, "pageNotFound404.html", status=404)


def petGET(request):
    title = request.GET.get('title')  # лучше применять когда есть форма
    return HttpResponse(f"<h2>{title}</h2>")


def categories(request, category_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{category_id}</p>")

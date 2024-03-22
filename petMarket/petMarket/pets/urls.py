from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index, name='main_url'),  # http://127.0.0.1:8000/pets/ == main_url
    path('petGET/', pets.petGET),
    path('<slug:pet_slug>/', pets.pet),
    path('categories/<int:category_id>/', pets.categories),
]

from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index),  # http://127.0.0.1:8000/pets/
    # path('cats/', pets.cats),
    # path('dogs/', pets.dogs),
    path('petGET/', pets.petGET),
    path('<slug:pet_slug>/', pets.pet),
    path('categories/<int:category_id>/', pets.categories),
]

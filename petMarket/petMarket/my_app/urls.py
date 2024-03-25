from django.urls import path, re_path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.index),
    path('products/<int:number_product>/', my_app.products),
]

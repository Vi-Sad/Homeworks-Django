from django.urls import path, re_path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.index),
    # path('my_app/page_1/', my_app.page_1),
    # path('my_app/page_2/', my_app.page_2),
    path('products/<int:number_product>/', my_app.products),
]

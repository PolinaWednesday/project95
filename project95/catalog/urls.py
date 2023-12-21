from django.urls import path
from catalog.views import index, contact, home

urlpatterns = [
    path('index/', index),
    path('contact/', contact),
    path('', home)
]

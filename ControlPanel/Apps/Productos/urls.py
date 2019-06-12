from django.urls import path
from Apps.Productos.views import index, insert, new

urlpatterns = [
    path(r'', index),
    path('new', new),
    path('insert', insert),
]
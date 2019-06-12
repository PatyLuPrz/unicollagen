from django.urls import path
from Apps.Productos.views import index

urlpatterns = [
    path(r'', index),
]
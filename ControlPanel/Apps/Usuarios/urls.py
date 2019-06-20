from django.urls import path
from Apps.Productos.views import index, insert, delete, view, update

urlpatterns = [
    path(r'', index),
    path('insert', insert),
    path('delete/', delete),
    path('update/', update),
    path('view/',view),
]
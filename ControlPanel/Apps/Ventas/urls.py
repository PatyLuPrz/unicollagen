from django.urls import path
from Apps.Ventas.views import view, index

urlpatterns = [
    path(r'', index),
    path('view/<int:id_venta>',view, name = 'view'),
]
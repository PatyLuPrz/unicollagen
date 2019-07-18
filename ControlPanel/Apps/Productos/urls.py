from django.urls import path
from Apps.Productos.views import index, insert, delete, update, view, ingles

urlpatterns = [
    path(r'', index, name = 'index'),
    path('insert', insert, name = 'insert'),
    path('insert/ingles', ingles, name = 'ingles'),
    path('delete/<int:id_producto>', delete, name = 'delete'),
    path('update/<int:id_producto>', update, name = 'update'),
    path('view/<int:id_producto>',view, name = 'view'),
]
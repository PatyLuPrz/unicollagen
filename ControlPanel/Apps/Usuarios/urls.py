from django.urls import path
from Apps.Usuarios.views import index, insert, delete, view, update

urlpatterns = [
    path(r'', index, name = 'index'),
    path('insert', insert, name = 'insert'),
    path('delete/<int:id_usuario>', delete, name = 'delete'),
    path('update/<int:id_usuario>', update, name = 'update'),
    path('view/<int:id_usuario>',view, name = 'view'),
]
from django.urls import path
from Apps.Usuarios.views import index, insert, delete, view, update

urlpatterns = [
    path(r'', index, name = 'index'),
    path('insert', insert, name = 'insert'),
    path('delete/', delete, name = 'delete'),
    path('update/', update, name = 'update'),
    path('view/',view, name = 'view'),
]
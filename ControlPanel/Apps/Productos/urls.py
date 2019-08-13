from django.urls import path
from Apps.Productos.views import index, insert, delete, update, view, ingles, otheringlesinsert, insertPrecios, updatePrecios, insertStock, updateStock


urlpatterns = [
    path(r'', index, name = 'index'),
    path('insert', insert, name = 'insert'),
    path('delete/<int:id_producto>', delete, name = 'delete'),
    path('update/<int:id_producto>', update, name = 'update'),
    path('update/precios/<int:id_producto>',updatePrecios,name='updateprecios'),
    path('update/stock/<int:id_producto>',updateStock,name='updatestock'),
    path('view/<int:id_producto>',view, name = 'view'),
    path('insert/ingles/<int:id_producto>',ingles, name = 'ingles'),
    path('other', otheringlesinsert, name = 'otherinsert'),
    path('insert/precios',insertPrecios,name="precios"),
    path('insert/stock',insertStock,name='insertstock')
]
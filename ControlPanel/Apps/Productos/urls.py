from django.urls import path
from Apps.Productos.views import index, insert, delete, update, view, ingles, otheringlesinsert, insertPrecios, updatePrecios, insertStock, updateStock, otheringlesupdate, insertPresentacion, updatePresentacion, deletePresentacion


urlpatterns = [
    path(r'', index, name = 'index'),
    path('insert', insert, name = 'insert'),
    path('delete/<int:id_producto>', delete, name = 'delete'),
    path('delete/presentacion/<int:id>', deletePresentacion, name = 'deletepresentacion'),
    path('update/<int:id_producto>', update, name = 'update'),
    path('update/precios/<int:id_producto>',updatePrecios,name='updateprecios'),
    path('update/presentacion/<int:id>',updatePresentacion,name='updatepresentacion'),
    path('update/stock/<int:id_producto>',updateStock,name='updatestock'),
    path('update/ingles/<int:id_producto>',otheringlesupdate,name='otheringlesupdate'),
    path('view/<int:id_producto>',view, name = 'view'),
    path('insert/ingles/<int:id_producto>',ingles, name = 'ingles'),
    path('others', otheringlesinsert, name = 'otherinsert'),
    path('insert/precios',insertPrecios,name="precios"),
    path('insert/stock',insertStock,name='insertstock'),
    path('insert/presentacion',insertPresentacion,name='insertpresentacion'),
]
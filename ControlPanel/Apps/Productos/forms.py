from django import forms
from Apps.Productos.models import Espanol, Frances, Ingles, Existencia, Precio

class EspanolForm(forms.ModelForm):
    class Meta:
        model = Espanol

        fields = [
            'nombre_producto',
            'marca_producto',
            'presentacion_producto',
            'tipo_producto',
            'descripcion_producto',
            'recomendacion_producto',
            'beneficios_producto',
        ]
        labels = {
            'nombre_producto':'Nombre del producto',
            'marca_producto':'Marca del producto',
            'presentacion_producto':'Tipo de presentacion del producto',
            'tipo_producto':'Tipo de producto',
            'descripcion_producto':'Descripcion del producto',
            'recomendacion_producto':'Recomendaciones de uso',
            'beneficios_producto':'Beneficios de uso',
        }
        
        selectPresentacion = [
            ('1','100 g'),
            ('2','50 g'),
            ('2','25 g'),
        ]
        selectTipo = [
            ('1','cremas'),
            ('2','otros'),
        ]

        widgets = {
            'nombre_producto':forms.TextInput(attrs={'class':'form-control'}),
            'marca_producto':forms.TextInput(attrs={'class':'form-control'}),
            'presentacion_producto':forms.Select(attrs={'class':'form-control'}, choices=selectPresentacion),
            'tipo_producto':forms.Select(attrs={'class':'form-control'}, choices=selectTipo),
            'descripcion_producto':forms.Textarea(attrs={'class':'form-control'}),
            'recomendacion_producto':forms.Textarea(attrs={'class':'form-control'}),
            'beneficios_producto':forms.Textarea(attrs={'class':'form-control'}),
        }



class InglesForm(forms.ModelForm):
    class Meta:
        model = Ingles

        fields = [
            'producto',
            'nombre_producto_ingles',
            'marca_producto_ingles',
            'presentacion_producto_ingles',
            'tipo_producto_ingles',
            'descripcion_producto_ingles',
            'recomendacion_producto_ingles',
            'beneficios_producto_ingles',
        ]
        labels = {
            'producto':'Producto al que pertenece esta traduccion',
            'nombre_producto_ingles':'Nombre del producto',
            'marca_producto_ingles_ingles':'Marca del producto',
            'presentacion_producto_ingles_ingles':'Tipo de presentacion del producto',
            'tipo_producto_ingles_ingles':'Tipo de producto',
            'descripcion_producto_ingles_ingles':'Descripcion del producto',
            'recomendacion_producto_ingles_ingles':'Recomendaciones de uso',
            'beneficios_producto_ingles_ingles':'Beneficios de uso',
        }
        
        selectPresentacion = [
            ('1','100 g'),
            ('2','50 g'),
            ('2','25 g'),
        ]
        selectTipo = [
            ('1','Creams'),
            ('2','Others'),
        ]

        widgets = {
            'producto':forms.Select(attrs={'class':'form-control'}),
            'nombre_producto_ingles':forms.TextInput(attrs={'class':'form-control'}),
            'marca_producto_ingles':forms.TextInput(attrs={'class':'form-control'}),
            'presentacion_producto_ingles':forms.Select(attrs={'class':'form-control'}, choices=selectPresentacion),
            'tipo_producto_ingles':forms.Select(attrs={'class':'form-control'}, choices=selectTipo),
            'descripcion_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
            'recomendacion_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
            'beneficios_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
        }



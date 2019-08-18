from django import forms
from Apps.Productos.models import Espanol, Ingles, Existencia, Precio, Presentacion

class EspanolForm(forms.ModelForm):
    class Meta:
        model = Espanol

        fields = [
            'foto_producto',
            'nombre_producto',
            'marca_producto',
            'tipo_producto',
            'descripcion_producto',
            'recomendacion_producto',
            'beneficios_producto',
        ]
        labels = {
            'foto_producto':'Foto del producto',
            'nombre_producto':'Nombre del producto',
            'marca_producto':'Marca del producto',
            'tipo_producto':'Tipo de producto',
            'descripcion_producto':'Descripcion del producto',
            'recomendacion_producto':'Recomendaciones de uso',
            'beneficios_producto':'Beneficios de uso',
        }
        
        selectTipo = [
            ('01','Shampoo'),
            ('02','Acondicionadores'),
            ('03','Lociones'),
            ('04','Aceites'),
            ('05','Cremas'),
            ('06','Talcos'),
            ('07','Productos para bebes - Niños'),
            ('08','Maquillaje'),
            ('09','Productos para el area de los ojos'),
            ('10','Polvos faciales'),
            ('11','Base de maquillaje'),
            ('12','Maquillaje para las piernas y cuerpo'),
            ('13','Lociones faciales'),
            ('14','Cremas para manos y cuerpo'),
            ('15','Mascaras faciales'),
            ('16','Otros cosmeticos para la piel'),
            ('17','Lápices labiales'),
            ('18','Brillo labial'),
            ('19','Otros productos para los labios'),
            ('20','Jabones'),
            ('21','Aceites de baño'),
            ('22','Tabletas de baño'),
            ('23','Sales de baño'),
            ('24','Burbujas y geles de baño'),
            ('25','Otros productos para el aseo e higiene corporal'),
            ('26','Desodorantes'),
            ('27','Productos para la hiegiene femenina'),
            ('28','Otros productos desodorantes y antitranspirantes'),
            ('29','Productos para el cabello'),
            ('30','Base de esmalte'),
            ('31','Crema para las uñas'),
            ('32','Esmalte'),
            ('33','Oleo para uñas'),
            ('34','Removedor de esmalte'),
            ('35','Otro producto para las uñas'),
            ('36','Detrificos (Todo tipo)'),
            ('37','Enjuagues bucales (No medicados)'),
            ('38','Otros productos para la higiene bucal y dental'),
            ('39','Bálsamo para después de afeitarse'),
            ('40','Lociones para después de afeitarse'),
            ('41','Cremas de afeitar'),
            ('42','Jabones y espumas de afeitar'),
            ('43','Otros productos de afeitar'),
            ('44','Aceites bronceadores'),
            ('45','Cremas bronceadoras'),
            ('46','Protectores solares'),
            ('47','Otros productos para el bronceado y proteccion solar'),
            ('48','Ceras depiladoras'),
            ('49','Cremas depiladoras'),
            ('50','Aceite depilatorio'),
            ('51','Gel depilatorio'),
            ('52','Cremas blanqueadoras'),
            ('53','Lociones blanqueadoras'),
            ('54','Otros productos para el blanqueado de la piel'),
            ('55','Otros'),
        ]

        widgets = {
            'foto_producto': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto':forms.TextInput(attrs={'class':'form-control'}),
            'marca_producto':forms.TextInput(attrs={'class':'form-control'}),
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
            'tipo_producto_ingles',
            'descripcion_producto_ingles',
            'recomendacion_producto_ingles',
            'beneficios_producto_ingles',
        ]
        labels = {
            'producto':'Producto al que pertenece esta traduccion',
            'nombre_producto_ingles':'Nombre del producto',
            'marca_producto_ingles_ingles':'Marca del producto',
            'tipo_producto_ingles_ingles':'Tipo de producto',
            'descripcion_producto_ingles_ingles':'Descripcion del producto',
            'recomendacion_producto_ingles_ingles':'Recomendaciones de uso',
            'beneficios_producto_ingles_ingles':'Beneficios de uso',
        }
        
        selectTipo = [
            ('01','Shampoo'),
            ('02','Conditioners'),
            ('03','Lotions'),
            ('04','Oils'),
            ('05','Creams'),
            ('06','Talc'),
            ('07','Products for babies - Children'),
            ('08','Makeup'),
            ('09','Products for the eye area'),
            ('10','Facial powders'),
            ('11','Makeup base'),
            ('12','Makeup for the legs and body'),
            ('13','Facial lotions'),
            ('14','Creams for hands and body'),
            ('15','Facial masks'),
            ('16','Other skin cosmetics'),
            ('17','Lipsticks'),
            ('18','Lip gloss'),
            ('19','Other products for lips'),
            ('20','Soaps'),
            ('21','Bath oils'),
            ('22','Bath tablets'),
            ('23','Bath salts'),
            ('24','Bubbles and bath gels'),
            ('25','Other products for hygiene and body hygiene'),
            ('26','Deodorants'),
            ('27','Products for female hiegiene'),
            ('28','Other deodorant and antiperspirant products'),
            ('29','Hair products'),
            ('30','Enamel base'),
            ('31','Nail cream'),
            ('32','Enamel'),
            ('33','Nail Oil'),
            ('34','Polish remover'),
            ('35','Another product for nails'),
            ('36','Detrificos (All types)'),
            ('37','Mouthwashes (Not medicated)'),
            ('38','Other products for oral and dental hygiene'),
            ('39','After shave balm'),
            ('40','After shave lotions'),
            ('41','Shaving creams'),
            ('42','Soaps and shaving foams'),
            ('43','Other shaving products'),
            ('44','Tanning oils'),
            ('45','Suntan creams'),
            ('46','Sunscreens'),
            ('47','Other products for tanning and sun protection'),
            ('48','Waxing Waxes'),
            ('49','Epilating creams'),
            ('50','Depilatory oil'),
            ('51','Depilatory gel'),
            ('52','Whitening creams'),
            ('53','Whitening lotions'),
            ('54','Other skin whitening products'),
            ('55','Others'),
        ]

        widgets = {
            'producto':forms.Select(attrs={'class':'form-control'}),
            'nombre_producto_ingles':forms.TextInput(attrs={'class':'form-control'}),
            'marca_producto_ingles':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_producto_ingles':forms.Select(attrs={'class':'form-control'}, choices=selectTipo),
            'descripcion_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
            'recomendacion_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
            'beneficios_producto_ingles':forms.Textarea(attrs={'class':'form-control'}),
        }

class PreciosForm(forms.ModelForm):
    class Meta:
        model = Precio

        fields = [
            'producto',
            'precio_peso_mx',
            'precio_dolar_eua',
            'precio_euro',
        ]

        labels = {
            'producto':'Producto al que pertenece estos precios',
            'precio_peso_mx':'Precio en peso mx',
            'precio_dolar_eua':'Precio en dolar estadounidense',
            'precio_euro':'Precio en euro',
        }

        widgets = {
            'producto':forms.Select(attrs={'class':'form-control'}),
            'precio_peso_mx':forms.NumberInput(attrs={'class':'form-control'}),
            'precio_dolar_eua':forms.NumberInput(attrs={'class':'form-control'}),
            'precio_euro':forms.NumberInput(attrs={'class':'form-control'}),
        }

    
class StockForm(forms.ModelForm):
    class Meta:
        model = Existencia

        fields = [
            'producto',
            'existencias',
        ]

        labels = {
            'producto':'Producto',
            'existencias':'Existencia en stock (No acumulable)',
        }

        widgets = {
            'producto':forms.Select(attrs={'class':'form-control'}),
            'existencias':forms.NumberInput(attrs={'class':'form-control'}),
        }

class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion

        fields = [
            'producto',
            'unidad_de_medida',
            'cantidad',
        ]

        labels = {
            'producto':'Producto',
            'unidad_de_medida':'Unidad de medida',
            'cantidad':'Cantidad',
        }

        selectUnidad = [
            ('01','Kilogramos'),
            ('02','Gramos'),
            ('03','Miligramos'),
            ('04','Litros'),
            ('05','Mililitros'),
            ('06','Onza'),
            ('07','Libra'),
        ]

        widgets = {
            'producto':forms.Select(attrs={'class':'form-control'}),
            'unidad_de_medida':forms.Select(attrs={'class':'form-control'}, choices=selectUnidad),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
        }
# Generated by Django 2.2.1 on 2019-06-07 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_espanol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=250)),
                ('precio_producto', models.FloatField()),
                ('marca_producto', models.CharField(max_length=250)),
                ('presentacion_producto', models.CharField(max_length=250)),
                ('tipo_producto', models.CharField(max_length=250)),
                ('descripcion_producto', models.TextField()),
                ('recomendacion_producto', models.TextField()),
                ('beneficios_producto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto_ingles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto_ingles', models.CharField(max_length=250)),
                ('precio_producto_ingles', models.FloatField()),
                ('marca_producto_ingles', models.CharField(max_length=250)),
                ('presentacion_producto_ingles', models.CharField(max_length=250)),
                ('tipo_producto_ingles', models.CharField(max_length=250)),
                ('descripcion_producto_ingles', models.TextField()),
                ('recomendacion_producto_ingles', models.TextField()),
                ('beneficios_producto_ingles', models.TextField()),
                ('producto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto_espanol')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_frances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto_frances', models.CharField(max_length=250)),
                ('precio_producto_frances', models.FloatField()),
                ('marca_producto_frances', models.CharField(max_length=250)),
                ('presentacion_producto_frances', models.CharField(max_length=250)),
                ('tipo_producto_frances', models.CharField(max_length=250)),
                ('descripcion_producto_frances', models.TextField()),
                ('recomendacion_producto_frances', models.TextField()),
                ('beneficios_producto_frances', models.TextField()),
                ('producto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto_espanol')),
            ],
        ),
        migrations.CreateModel(
            name='Existencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencias', models.IntegerField()),
                ('producto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto_espanol')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-25 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('apellido_paterno_cliente', models.CharField(max_length=255)),
                ('apellido_materno_cliente', models.CharField(max_length=255)),
                ('correo_cliente', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle_direccion', models.CharField(max_length=255)),
                ('colonia_direccion', models.CharField(max_length=255)),
                ('numero_ext_direccion', models.CharField(max_length=15)),
                ('numero_int_direccion', models.CharField(max_length=15)),
                ('ciudad_direccion', models.CharField(max_length=255)),
                ('estado_direccion', models.CharField(max_length=255)),
                ('pais_direccion', models.CharField(max_length=255)),
                ('codigo_postal_direccion', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_a_pagar_venta', models.FloatField()),
                ('total_productos_venta', models.IntegerField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.Cliente')),
                ('direccion_envio_venta', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencia', models.IntegerField()),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Espanol')),
                ('venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.Venta')),
            ],
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-18 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_auto_20190818_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espanol',
            old_name='foto_produto',
            new_name='foto_producto',
        ),
    ]
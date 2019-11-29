# Generated by Django 2.2.7 on 2019-11-28 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('categoria_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='producto.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=250)),
                ('url_imagen', models.CharField(max_length=250, verbose_name='URL')),
                ('precio_unidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unidad')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.Categoria')),
            ],
        ),
    ]

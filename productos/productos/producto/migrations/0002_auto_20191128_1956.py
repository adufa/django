# Generated by Django 2.2.7 on 2019-11-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_unidad',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='url_imagen',
            field=models.CharField(max_length=250),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residencias', '0002_auto_20191128_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='fecha_informe',
            field=models.DateField(),
        ),
    ]

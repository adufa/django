# Generated by Django 2.2.7 on 2019-11-28 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=144)),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_salida', models.DateTimeField()),
                ('fecha_llegada', models.DateTimeField()),
                ('codigo_vuelo', models.CharField(max_length=10)),
                ('aeropuerto_llegada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuelo.Aeropuerto')),
                ('aeropuerto_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vuelo.Aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateTimeField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuelo.Cliente')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuelo.Vuelo')),
            ],
        ),
    ]

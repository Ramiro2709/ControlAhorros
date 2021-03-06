# Generated by Django 3.1.5 on 2021-02-11 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_auto_20210211_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_fondo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('interes', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.categoria'),
        ),
        migrations.CreateModel(
            name='Fondo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=10, max_digits=20)),
                ('moneda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.moneda')),
                ('subcategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.subcategoria')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.tipo_fondo')),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-11 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='moneda_origen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.moneda'),
        ),
        migrations.AddField(
            model_name='log',
            name='subcat_dest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='Registro.subcategoria'),
        ),
        migrations.AddField(
            model_name='log',
            name='subcat_origen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='Registro.subcategoria'),
        ),
        migrations.AlterField(
            model_name='tipo_log',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
    ]

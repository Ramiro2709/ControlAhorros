# Generated by Django 3.1.5 on 2021-02-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0006_auto_20210214_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='plataforma_des',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='Registro.plataforma'),
        ),
        migrations.AddField(
            model_name='log',
            name='plataforma_or',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='Registro.plataforma'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20210211_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='valorBTC',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='log',
            name='valorDAI',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-27 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0010_auto_20210226_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_trade',
            name='id',
        ),
        migrations.AddField(
            model_name='log_trade',
            name='log_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Registro.log'),
            preserve_default=False,
        ),
    ]

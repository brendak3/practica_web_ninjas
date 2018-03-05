# Generated by Django 2.0.1 on 2018-02-25 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equiponinja',
            name='capitan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Capitan'),
        ),
        migrations.RemoveField(
            model_name='equiponinja',
            name='integrantes',
        ),
        migrations.AddField(
            model_name='equiponinja',
            name='integrantes',
            field=models.ManyToManyField(to='equipos.Ninja'),
        ),
    ]
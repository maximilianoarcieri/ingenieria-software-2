# Generated by Django 4.0.3 on 2022-05-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_auto_20220117_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bon',
            name='nbDeployOrdered',
            field=models.CharField(blank=True, choices=[('3', 3), ('6', 6), ('9', 9), ('12', 12)], max_length=255, null=True, verbose_name='Nombre de mise en ligne commandées'),
        ),
    ]

# Generated by Django 3.2.9 on 2023-02-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_entreprise_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Titre'),
        ),
    ]
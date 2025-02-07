# Generated by Django 3.2.9 on 2022-01-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_entreprise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='localisation',
        ),
        migrations.AddField(
            model_name='entreprise',
            name='city',
            field=models.CharField(default='paris', max_length=255, verbose_name='Ville'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entreprise',
            name='streetName',
            field=models.CharField(default='rue planchat, 75020 paris, France', max_length=255, verbose_name='Nom de la rue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entreprise',
            name='streetNumber',
            field=models.CharField(default='2', max_length=255, verbose_name='Numéro de rue'),
            preserve_default=False,
        ),
    ]

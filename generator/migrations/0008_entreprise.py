# Generated by Django 3.2.9 on 2022-01-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0007_alter_bon_nbdeployordered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('localisation', models.CharField(max_length=255, verbose_name='localisation')),
                ('phoneNumber', models.CharField(max_length=255, verbose_name='numéro de téléphone')),
                ('job', models.CharField(max_length=255, verbose_name='Job')),
            ],
        ),
    ]

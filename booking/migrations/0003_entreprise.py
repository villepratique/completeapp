# Generated by Django 3.2.9 on 2022-01-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_contact_message'),
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

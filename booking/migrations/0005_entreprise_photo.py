# Generated by Django 3.2.9 on 2022-01-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20220118_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='soc_photos'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

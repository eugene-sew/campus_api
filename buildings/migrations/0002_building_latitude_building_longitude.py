# Generated by Django 5.0.6 on 2024-09-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

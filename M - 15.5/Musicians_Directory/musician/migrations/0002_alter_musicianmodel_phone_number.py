# Generated by Django 5.0.4 on 2024-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='Phone_number',
            field=models.CharField(max_length=12),
        ),
    ]

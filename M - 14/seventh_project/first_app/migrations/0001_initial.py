# Generated by Django 5.0.4 on 2024-05-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
    ]

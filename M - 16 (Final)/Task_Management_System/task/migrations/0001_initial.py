# Generated by Django 5.0.4 on 2024-05-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('Task_Assign_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-22 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('horsepower', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.car')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]

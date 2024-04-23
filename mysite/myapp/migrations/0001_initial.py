# Generated by Django 5.0.2 on 2024-04-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('temperature', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('humidity', models.CharField(max_length=500, null=True)),
                ('pressure', models.CharField(max_length=500, null=True)),
                ('wind_speed', models.CharField(max_length=500, null=True)),
                ('visibility', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]

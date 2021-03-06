# Generated by Django 3.2.6 on 2022-06-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=250)),
                ('rating', models.FloatField()),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Police_Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=250)),
                ('rating', models.FloatField()),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AZFlag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(max_length=20)),
                ('imgURL', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

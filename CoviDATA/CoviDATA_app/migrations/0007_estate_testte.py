# Generated by Django 3.0.9 on 2020-08-09 03:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoviDATA_app', '0006_remove_estate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='testte',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, default=0, size=None),
            preserve_default=False,
        ),
    ]
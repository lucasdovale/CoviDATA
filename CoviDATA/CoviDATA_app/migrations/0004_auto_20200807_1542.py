# Generated by Django 3.0.9 on 2020-08-07 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoviDATA_app', '0003_estate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estate',
            name='casos',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='medmov_casos',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='medmov_obitos',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='obitos',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='recuperados',
        ),
    ]

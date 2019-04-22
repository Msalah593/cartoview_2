# Generated by Django 2.2 on 2019-04-22 20:01

import cartoview.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_manager', '0003_auto_20190422_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='default_config',
            field=cartoview.fields.DictField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='appinstance',
            name='config',
            field=cartoview.fields.DictField(blank=True, default=None, null=True),
        ),
    ]
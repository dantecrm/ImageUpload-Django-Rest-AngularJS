# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_scramble_uploaded_filename_20160816_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Thumbnail of uploaded image'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('Pub_date', models.DateTimeField(verbose_name='date published')),
                ('image_link', models.CharField(max_length=200)),
                ('text_link', models.CharField(max_length=200)),
            ],
        ),
    ]

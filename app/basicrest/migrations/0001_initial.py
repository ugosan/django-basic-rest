# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=36, db_index=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('race', models.CharField(default=b'DOG', max_length=6, db_index=True, choices=[(b'DOG', 'Dog'), (b'CAT', 'Cat'), (b'COCKATIEL', 'Cockatiel')])),
            ],
        ),
        migrations.CreateModel(
            name='PetActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('activity', models.CharField(db_index=True, max_length=4, null=True, choices=[(b'FEED', 'Feed'), (b'WALK', 'Walk'), (b'PLAY', 'Play')])),
                ('pet', models.ForeignKey(related_name='activities', verbose_name='Activities', to='basicrest.Pet')),
            ],
        ),
    ]

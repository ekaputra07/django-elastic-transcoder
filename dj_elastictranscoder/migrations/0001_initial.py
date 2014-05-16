# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncodeJob',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', to_field='id')),
                ('object_id', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField(default=0, db_index=True, choices=[(0, b'Submitted'), (1, b'Progressing'), (2, b'Error'), (3, b'Warning'), (4, b'Complete')])),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-02 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, b'todo'), (2, b'doing'), (3, b'done')])),
            ],
        ),
        migrations.CreateModel(
            name='user_db',
            fields=[
                ('username', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('usertype', models.PositiveSmallIntegerField(choices=[(1, b'admin'), (2, b'student')])),
                ('password', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='task_table',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.user_db'),
        ),
        migrations.AddField(
            model_name='task_table',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='quickstart.user_db'),
        ),
    ]

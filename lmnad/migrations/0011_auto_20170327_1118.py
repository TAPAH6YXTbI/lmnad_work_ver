# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-27 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmnad', '0010_auto_20170207_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='reference_result',
            field=models.CharField(blank=True, max_length=500, verbose_name='C\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043a\u043e\u043d\u043a\u0443\u0440\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='abstract',
            field=models.TextField(blank=True, verbose_name='\u0410\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f'),
        ),
        migrations.RemoveField(
            model_name='grant',
            name='head',
        ),
        migrations.AddField(
            model_name='grant',
            name='head',
            field=models.ManyToManyField(related_name='head', to='lmnad.People', verbose_name='\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='members',
            field=models.ManyToManyField(related_name='members', to='lmnad.People', verbose_name='\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='number',
            field=models.CharField(max_length=50, verbose_name='\u041d\u043e\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='reference',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0433\u0440\u0430\u043d\u0442'),
        ),
    ]

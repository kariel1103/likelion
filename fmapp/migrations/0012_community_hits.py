# Generated by Django 3.2.5 on 2021-08-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmapp', '0011_auto_20210812_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='์กฐํ์'),
        ),
    ]

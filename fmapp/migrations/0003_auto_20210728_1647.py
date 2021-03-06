# Generated by Django 3.2.5 on 2021-07-28 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fmapp', '0002_auto_20210722_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='community',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='최종수정일'),
        ),
        migrations.AlterField(
            model_name='community',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]

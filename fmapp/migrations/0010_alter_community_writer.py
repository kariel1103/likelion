# Generated by Django 3.2.6 on 2021-08-12 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('fmapp', '0009_community_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_appusermodel_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appusermodel',
            name='role',
        ),
    ]
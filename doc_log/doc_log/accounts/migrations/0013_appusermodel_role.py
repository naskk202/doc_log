# Generated by Django 4.0.3 on 2022-04-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_appusermodel_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='appusermodel',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'Doctor'), (2, 'Patient')], default=1),
            preserve_default=False,
        ),
    ]
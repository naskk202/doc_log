# Generated by Django 4.0.3 on 2022-04-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_doctorsmodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsmodel',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile_pics'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-18 17:49

from django.db import migrations, models
import doc_log.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_doctorsmodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsmodel',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/images/static_images/auto_doc_pic.png', null=True, upload_to='static/images/profile_pics', validators=[doc_log.common.validators.image_size_validator_in_mb]),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-16 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doc_log_app', '0008_alter_visitationmodel_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitationmodel',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

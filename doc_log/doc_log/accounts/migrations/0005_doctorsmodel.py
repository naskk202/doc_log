# Generated by Django 4.0.3 on 2022-04-03 12:59

import django.core.validators
from django.db import migrations, models
import doc_log.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_patientmodel_egn'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), doc_log.common.validators.only_char_validator])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), doc_log.common.validators.only_char_validator])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='static')),
                ('specialisation', models.CharField(choices=[('Pediatrician', 'Pediatrician'), ('Neurologist', 'Neurologist'), ('Dermatologist', 'Dermatologist'), ('Surgeon', 'Surgeon'), ('virologist', 'virologist'), ('cardiologist', 'cardiologist'), ('ENT', 'ENT'), ('Gynecologist', 'Gynecologist'), ('Urologist', 'Urologist'), ('Dentist', 'Dentist')], max_length=13)),
                ('work_time_from', models.DateTimeField()),
                ('work_time_to', models.DateTimeField()),
                ('address', models.TextField()),
                ('education', models.TextField(blank=True, null=True)),
                ('qualification', models.TextField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

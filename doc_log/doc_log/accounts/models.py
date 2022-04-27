from os import path

from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models

from doc_log.accounts.managers import AppUserManager
from doc_log.common.validators import only_char_validator, only_digit_validator, \
    image_size_validator_in_mb


class AppUserModel(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25

    DOCTOR = 1
    PATIENT = 2

    ROLE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    role = models.SmallIntegerField(
        choices=ROLE_CHOICES,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class PatientModel(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    EGN_LEN = 10

    PHONE_NUMBER_MAX_LEN = 14
    PHONE_NUMBER_MIN_LEN = 6

    FREE_TEXT_MAX_LEN = 120

    BLOOD_GROUPS = (
        ('None', 'None'),
        ('0-', '0-'),
        ('0+', '0+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    )

    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_char_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_char_validator,
        )
    )

    age = models.IntegerField()

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
    )

    egn = models.CharField(
        max_length=EGN_LEN,
        unique=True,

        validators=(
            MinLengthValidator(EGN_LEN),
            only_digit_validator,
        )
    )

    #   --- not required---
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LEN,
        blank=True,
        null=True,

        validators=(
            only_digit_validator,
        )
    )

    blood_type = models.CharField(
        max_length=4,
        choices=BLOOD_GROUPS,
        default='None',
    )

    allergens = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )
    operations = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )
    vaccines = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AppUserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SpecialisationModel(models.Model):
    SPECIALISATION = (
        ('1', 'Pediatrician'),
        ('2', 'Neurologist'),
        ('3', 'Dermatologist'),
        ('4', 'Surgeon'),
        ('5', 'Virologist'),
        ('6', 'Cardiologist'),
        ('7', 'ENT'),
        ('8', 'Gynecologist'),
        ('9', 'Urologist'),
        ('10', 'Dentist'),
    )
    specialisation = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.specialisation


class DoctorsModel(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    FREE_TEXT_MAX_LEN = 120

    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_char_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_char_validator,
        )
    )

    work_time_from = models.TimeField()

    work_time_to = models.TimeField()

    address = models.TextField()

    #   --- not required---
    profile_picture = cloudinary_models.CloudinaryField('image')

    # models.ImageField(
    # upload_to=path.join('static/images/profile_pics'),
    # blank=True,
    # null=True,
    # validators=(
    #     image_size_validator_in_mb,
    # This can make problem
    # if someone uploads a 1TB file, I probably run out of hard drive space before the user gets a form error
    #     )
    # )
    education = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )

    qualification = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )

    biography = models.CharField(
        max_length=FREE_TEXT_MAX_LEN,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AppUserModel,
        on_delete=models.CASCADE,
        primary_key=True,

    )

    specialisation = models.ForeignKey(
        SpecialisationModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

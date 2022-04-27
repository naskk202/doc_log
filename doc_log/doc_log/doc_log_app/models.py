from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from doc_log.accounts.models import DoctorsModel, PatientModel, AppUserModel


class VisitationModel(models.Model):
    VISITATION_LEN_FIELDS = 120

    diagnose = models.CharField(
        max_length=VISITATION_LEN_FIELDS,
    )

    physical_signature = models.CharField(
        max_length=VISITATION_LEN_FIELDS,
    )

    condition = models.TextField()

    #   --- not required---
    drugs = models.CharField(
        max_length=VISITATION_LEN_FIELDS,
        blank=True,
        null=True,
    )

    next_appointment_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    date_of_visitation = models.DateField(
        auto_now_add=True,
    )

    doctor = models.ForeignKey(
        AppUserModel,
        on_delete=models.CASCADE,  # here it must be models.DO_NOTHING and set user to delete=True
    )

    # Form will give eng for this
    patient = models.ForeignKey(
        PatientModel,
        on_delete=models.CASCADE,
    )


class DoctorReviewModel(models.Model):
    MAX_COMMENT_LEN = 150

    comment = models.CharField(
        max_length=MAX_COMMENT_LEN
    )

    rating = models.IntegerField(
        default=0,
        validators=(
            MaxValueValidator(5),
            MinValueValidator(0),
        )
    )

    patient = models.ForeignKey(
        AppUserModel,
        on_delete=models.CASCADE,   # here it must be models.DO_NOTHING and set user to delete=True
    )

    doctor = models.ForeignKey(
        DoctorsModel,
        on_delete=models.CASCADE,
    )

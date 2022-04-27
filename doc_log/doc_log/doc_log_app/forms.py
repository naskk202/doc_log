from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator

from doc_log.accounts.models import PatientModel, DoctorsModel
from doc_log.common.helpers import BootstrapFormMixin
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from doc_log.common.validators import only_digit_validator
from doc_log.doc_log_app.models import VisitationModel, DoctorReviewModel

UserModel = get_user_model()


class VisitationForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    class Meta:
        model = VisitationModel
        exclude = ('doctor', 'patient', 'date_of_visitation', 'next_appointment_date')

    egn = forms.CharField(
        max_length=PatientModel.EGN_LEN,

        validators=(
            MinLengthValidator(PatientModel.EGN_LEN),
            MaxLengthValidator(PatientModel.EGN_LEN),
            only_digit_validator,
        )
    )

    diagnose = forms.CharField(
        max_length=VisitationModel.VISITATION_LEN_FIELDS,
    )

    physical_signature = forms.CharField(
        max_length=VisitationModel.VISITATION_LEN_FIELDS,
    )

    condition = forms.Textarea()

    #   --- not required---
    drugs = forms.CharField(
        max_length=VisitationModel.VISITATION_LEN_FIELDS,
        required=False,
    )

    next_appointment_date = forms.Field(
        required=False,
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user = VisitationModel(
            diagnose=self.cleaned_data['diagnose'],
            physical_signature=self.cleaned_data['physical_signature'],
            condition=self.cleaned_data['condition'],
            drugs=self.cleaned_data['drugs'],
            next_appointment_date=self.data['next-appointment-date-time'],
            patient=PatientModel.objects.get(egn=self.cleaned_data['egn']),
            doctor=self.user
        )

        if commit:
            user.save()

        return user


class DoctorReviewForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user[0]
        self.doctor = user[1]
        self._init_bootstrap_form_controls()

    class Meta:
        model = DoctorReviewModel
        exclude = ('patient', 'doctor')

    comment = forms.CharField(
        max_length=DoctorReviewModel.MAX_COMMENT_LEN,
    )

    rating = forms.IntegerField(
        validators=(
            MaxValueValidator(5),
            MinValueValidator(0),
        )
    )

    def save(self, commit=True):
        user = super().save(commit=False)

        user = DoctorReviewModel(
            comment=self.cleaned_data['comment'],
            rating=self.cleaned_data['rating'],
            doctor=DoctorsModel.objects.get(user_id=self.doctor),
            patient=self.user,
        )
        if commit:
            user.save()
        return user

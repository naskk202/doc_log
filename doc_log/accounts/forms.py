from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator, MaxLengthValidator

from doc_log.accounts.models import AppUserModel, PatientModel, DoctorsModel
from doc_log.common.helpers import BootstrapFormMixin
from doc_log.common.validators import only_char_validator, only_digit_validator, image_size_validator_in_mb

UserModel = get_user_model()


class PatientRegistrationForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(
        max_length=PatientModel.FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(PatientModel.FIRST_NAME_MIN_LENGTH),
            MaxLengthValidator(PatientModel.FIRST_NAME_MAX_LENGTH),
            only_char_validator,
        )
    )

    last_name = forms.CharField(
        max_length=PatientModel.LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(PatientModel.LAST_NAME_MIN_LENGTH),
            MaxLengthValidator(PatientModel.LAST_NAME_MAX_LENGTH),
            only_char_validator,
        )
    )

    age = forms.IntegerField()

    gender = forms.ChoiceField(
        choices=PatientModel.GENDERS,
    )

    egn = forms.CharField(
        max_length=PatientModel.EGN_LEN,

        validators=(
            MinLengthValidator(PatientModel.EGN_LEN),
            MaxLengthValidator(PatientModel.EGN_LEN),
            only_digit_validator,
        )
    )

    #   --- not required---
    phone_number = forms.CharField(
        max_length=PatientModel.PHONE_NUMBER_MAX_LEN,
        required=False,

        validators=(
            MinLengthValidator(PatientModel.PHONE_NUMBER_MIN_LEN),
            MaxLengthValidator(PatientModel.PHONE_NUMBER_MAX_LEN),
            only_digit_validator,
        )
    )

    blood_type = forms.ChoiceField(
        choices=PatientModel.BLOOD_GROUPS,
        required=False,
    )

    allergens = forms.CharField(
        max_length=PatientModel.FREE_TEXT_MAX_LEN,
        required=False,
    )

    operations = forms.CharField(
        max_length=PatientModel.FREE_TEXT_MAX_LEN,
        required=False,
    )

    vaccines = forms.CharField(
        max_length=PatientModel.FREE_TEXT_MAX_LEN,
        required=False,
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = AppUserModel.PATIENT
        user.save()

        patient = PatientModel(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            gender=self.cleaned_data['gender'],
            egn=self.cleaned_data['egn'],
            phone_number=self.cleaned_data['phone_number'],
            blood_type=self.cleaned_data['blood_type'],
            allergens=self.cleaned_data['allergens'],
            operations=self.cleaned_data['operations'],
            vaccines=self.cleaned_data['vaccines'],
            user=user,
        )

        if commit:
            patient.save()

        return user


class PatientEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PatientModel
        exclude = ('user',)


class DoctorRegistrationForm(BootstrapFormMixin, auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(
        max_length=PatientModel.FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(PatientModel.FIRST_NAME_MIN_LENGTH),
            MaxLengthValidator(PatientModel.FIRST_NAME_MAX_LENGTH),
            only_char_validator,
        )
    )

    last_name = forms.CharField(
        max_length=PatientModel.LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(PatientModel.LAST_NAME_MIN_LENGTH),
            MaxLengthValidator(PatientModel.LAST_NAME_MAX_LENGTH),
            only_char_validator,
        )
    )

    profile_picture = forms.ImageField(
        required=False,
        validators=(
            image_size_validator_in_mb,
        )
    )

    specialisation = forms.ChoiceField(
        choices=DoctorsModel.SPECIALISATION
        #choices=((el.id, el.specialisation) for el in SpecialisationModel.objects.all())
        # SpecialisationModel.SPECIALISATION

    )

    # work_time_from = forms.TimeField(
    #     widget=(
    #         forms.TimeInput(format='%H:%M')
    #     )
    # )
    #
    # work_time_to = forms.TimeField(
    #     widget=(
    #         forms.TimeInput(format='%H:%M')
    #     )
    # )

    address = forms.CharField(
        max_length=DoctorsModel.FREE_TEXT_MAX_LEN,
    )

    education = forms.CharField(
        max_length=DoctorsModel.FREE_TEXT_MAX_LEN,
        required=False,
    )

    qualification = forms.CharField(
        max_length=DoctorsModel.FREE_TEXT_MAX_LEN,
        required=False
    )

    biography = forms.CharField(
        max_length=DoctorsModel.FREE_TEXT_MAX_LEN,
        required=False
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = AppUserModel.DOCTOR
        user.is_staff = True
        user.save()

        doctor = DoctorsModel(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            # specialisation=SpecialisationModel.objects.get(pk=self.cleaned_data['specialisation']),
            specialisation=self.cleaned_data['specialisation'],
            work_time_from=self.data['work-time-from'],
            work_time_to=self.data['work-time-to'],
            address=self.cleaned_data['address'],
            education=self.cleaned_data['education'],
            qualification=self.cleaned_data['qualification'],
            biography=self.cleaned_data['biography'],
            user=user,
        )
        if commit:
            Group.objects.get(name='doctors_group').user_set.add(user.id)
            doctor.save()
        return user


class DoctorEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = DoctorsModel
        exclude = ('user', 'specialisation')


class DeleteUserForm(forms.ModelForm):
    # def save(self, commit=True):
    #     self.instance.delete()
    #     return self.instance

    class Meta:
        model = AppUserModel
        fields = ()

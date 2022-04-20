from django.core.exceptions import ValidationError
from django.test import TestCase

from doc_log.accounts.models import DoctorsModel, AppUserModel, SpecialisationModel


class DoctorsModelTest(TestCase):
    USER_VALID_DATA = {
        'email': "test@test.ts",
        'role': '1'
    }

    SPECIALISATION = {
        'specialisation': 'test'
    }

    VALID_DOCTOR_DATA = {
        'first_name': 'test',
        'last_name': 'test',
        'work_time_from': '10:10',
        'work_time_to': '11:11',
        'address': 'some address',
    }

    def test_doctor_create_imagefield__when_image_size_is_valid(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()
        specialisation = SpecialisationModel(**self.SPECIALISATION)
        specialisation.save()

        doctor = DoctorsModel(
            **self.VALID_DOCTOR_DATA,
            user=user,
            specialisation=specialisation,
            profile_picture='static/images/images_for_size_test/small_image.png',
        )
        doctor.save()
        self.assertIsNotNone(doctor.pk)

    def test_doctor_create_imagefield__when_image_size_is_invalid(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()
        specialisation = SpecialisationModel(**self.SPECIALISATION)
        specialisation.save()

        doctor = DoctorsModel(
            **self.VALID_DOCTOR_DATA,
            user=user,
            specialisation=specialisation,
            profile_picture='static/images/images_for_size_test/image_over_5mb.jpg',
        )

        with self.assertRaises(ValidationError) as context:
            doctor.full_clean()
            doctor.save()

        self.assertIsNotNone(context.exception)

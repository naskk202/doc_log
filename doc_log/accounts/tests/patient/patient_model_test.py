from django.core.exceptions import ValidationError
from django.test import TestCase

from doc_log.accounts.models import PatientModel, AppUserModel


class PatientModelTest(TestCase):
    USER_VALID_DATA = {
        'email': "test@test.ts",
        'role': '2'
    }

    VALID_PATIENT_DATA = {
        'first_name': 'test',
        'last_name': 'test',
        'age': '10',
        'gender': 'Male',
        'egn': '1234567890',
    }

    def test_patient_create__when_first_name_contains_only_letters__expect_success(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        patient = PatientModel(
            **self.VALID_PATIENT_DATA,
            user=user,
        )
        patient.save()
        self.assertIsNotNone(patient.pk)

    def test_patient_create__when_first_name_contains_a_digit__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        first_name = 'test1'

        patient = PatientModel(
            first_name=first_name,
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=self.VALID_PATIENT_DATA['egn'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_first_name_contains_a_bracket__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        first_name = 'te)st'

        patient = PatientModel(
            first_name=first_name,
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=self.VALID_PATIENT_DATA['egn'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_first_name_contains_a_space__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        first_name = 'te st'

        patient = PatientModel(
            first_name=first_name,
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=self.VALID_PATIENT_DATA['egn'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_egn_contains_a_letter__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        egn = '01234a6789'

        patient = PatientModel(
            first_name=self.VALID_PATIENT_DATA['first_name'],
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=egn,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_egn_contains_a_bracket__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        egn = '01234)6789'

        patient = PatientModel(
            first_name=self.VALID_PATIENT_DATA['first_name'],
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=egn,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_egn_contains_a_space__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        egn = '012345 6789'

        patient = PatientModel(
            first_name=self.VALID_PATIENT_DATA['first_name'],
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=egn,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_egn_is_with_nine_digits__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        egn = '012345678'

        patient = PatientModel(
            first_name=self.VALID_PATIENT_DATA['first_name'],
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=egn,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)

    def test_patient_create__when_egn_is_with_eleven_digits__expect_to_fail(self):
        user = AppUserModel(**self.USER_VALID_DATA)
        user.save()

        egn = '01234567899'

        patient = PatientModel(
            first_name=self.VALID_PATIENT_DATA['first_name'],
            last_name=self.VALID_PATIENT_DATA['last_name'],
            age=self.VALID_PATIENT_DATA['age'],
            gender=self.VALID_PATIENT_DATA['gender'],
            egn=egn,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            patient.full_clean()
            patient.save()

        self.assertIsNotNone(context.exception)
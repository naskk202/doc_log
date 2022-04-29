from django import template

from doc_log.accounts.models import AppUserModel

register = template.Library()


@register.filter(name='doctor')
def doctor_filter(value):
    return value == AppUserModel.DOCTOR


@register.filter(name='patient')
def patient_filter(value):
    return value == AppUserModel.PATIENT


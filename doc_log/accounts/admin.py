from django.contrib import admin

from doc_log.accounts.models import PatientModel, DoctorsModel, AppUserModel, SpecialisationModel


@admin.register(SpecialisationModel)
class SpecialisationAdmin(admin.ModelAdmin):
    pass

@admin.register(AppUserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_superuser')


@admin.register(PatientModel)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorsModel)
class DoctorAdmin(admin.ModelAdmin):
    pass



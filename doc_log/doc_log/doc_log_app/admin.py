from django.contrib import admin

# Register your models here.
from doc_log.doc_log_app.models import VisitationModel, DoctorReviewModel


@admin.register(VisitationModel)
class VisitationAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorReviewModel)
class DoctorReviewAdmin(admin.ModelAdmin):
    pass

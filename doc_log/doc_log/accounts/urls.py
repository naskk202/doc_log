from django.urls import path

from doc_log.accounts.views.doctor_views import CreateDoctorView, DoctorDetailView, EditDoctorView
from doc_log.accounts.views.patient_views import CreatePatientView, PatientDetailsView, EditPatientView, \
    search_patient
from doc_log.accounts.views.views import UserLoginView, logout_view, DeleteUserView, ChangePasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/<int:pk>', ChangePasswordView.as_view(), name='change password'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(), name='delete user'),

    path('patient-registration/', CreatePatientView.as_view(), name='patient registration'),
    path('patient-edit/<int:pk>/', EditPatientView.as_view(), name='patient edit'),
    path('patient-profile/<int:pk>/', PatientDetailsView.as_view(), name='patient details'),
    path('search-patient/', search_patient, name='search patient'),

    path('doctor-registration/', CreateDoctorView.as_view(), name='doctor registration'),
    path('doctor-edit/<int:pk>/', EditDoctorView.as_view(), name='doctor edit'),
    path('doctor-profile/<int:pk>/', DoctorDetailView.as_view(), name='doctor details'),

)

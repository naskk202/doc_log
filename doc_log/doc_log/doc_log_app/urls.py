from django.urls import path

from doc_log.doc_log_app.views import HomeView, SpecialistsView, VisitationView, DoctorReviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', SpecialistsView.as_view(), name='specialists'),
    path('visitation/<int:pk>/', VisitationView.as_view(), name='visitation'),
    path('doctor-review/<int:pk>/', DoctorReviewView.as_view(), name='doctor review'),

]

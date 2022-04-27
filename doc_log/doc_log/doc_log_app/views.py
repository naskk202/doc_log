from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from doc_log.accounts.models import DoctorsModel
from doc_log.common.helpers import in_doctors_group_check
from doc_log.doc_log_app.forms import VisitationForm, DoctorReviewForm
from doc_log.doc_log_app.models import VisitationModel, DoctorReviewModel


class HomeView(views.TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     specialisation = SpecialisationModel.objects.all()
    #
    #     context.update({
    #         'specialisations': specialisation,
    #     })
    #
    #     return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        specialisation = DoctorsModel.SPECIALISATION

        context.update({
            'specialisations': specialisation,
        })

        return context


class SpecialistsView(views.ListView):
    model = DoctorsModel
    template_name = 'doc_log/specialists_list.html'
    paginate_by = 10

    def get_queryset(self):
        docs = self.model.objects.filter(specialisation=self.kwargs['pk']).distinct()

        return docs


class VisitationView(LoginRequiredMixin, PermissionRequiredMixin,
                     views.CreateView):  # do I need the LoginRequiredMixin here?
    permission_required = ('doc_log_app.add_visitationmodel',)
    model = VisitationModel
    form_class = VisitationForm
    template_name = 'doc_log/visitation.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('patient details', kwargs={'pk': self.object.patient_id})


class DoctorReviewView(LoginRequiredMixin, views.CreateView):
    model = DoctorReviewModel
    form_class = DoctorReviewForm
    template_name = 'doc_log/doctor_review.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs = {
        #     'user': self.request.user,
        #     'doctor': self.kwargs.get('pk')
        # }
        # why i cant do it like this?
        kwargs['user'] = (self.request.user, self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self):
        return reverse('doctor details', kwargs={'pk': self.kwargs.get('pk')})



from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from doc_log.accounts.forms import PatientRegistrationForm, PatientEditForm
from doc_log.accounts.models import PatientModel
from doc_log.doc_log_app.models import VisitationModel


class CreatePatientView(views.CreateView):
    form_class = PatientRegistrationForm
    template_name = 'account/create_patient.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('home')


class EditPatientView(views.UpdateView):
    model = PatientModel
    form_class = PatientEditForm
    template_name = 'account/edit_patient.html'

    def get_success_url(self):
        return reverse('doctor details', kwargs={'pk': self.kwargs.get('pk')})


class PatientDetailsView(views.DetailView):
    model = PatientModel
    template_name = 'account/patient_info.html'

    def get_queryset(self):
        return PatientModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_owner = self.object.user_id == self.request.user.id
        activities = self.get_related_activities()

        context.update({
            'is_owner': is_owner,
            'page_obj': activities
        })

        return context

    def get_related_activities(self):
        queryset = VisitationModel.objects.filter(patient=self.object.user_id).distinct()
        paginator = Paginator(queryset, 2)  # paginate_by
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities


def search_patient(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            patient = PatientModel.objects.get(egn=searched)
            return render(request, 'account/search_patient.html', context={'patient': patient})
        except:
            return render(request, 'account/search_patient.html', context={'searched': searched})

    return render(request, 'account/search_patient.html')

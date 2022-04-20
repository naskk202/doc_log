from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.db.models import Sum, Avg
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from doc_log.accounts.forms import DoctorRegistrationForm, DoctorEditForm, DeleteUserForm
from doc_log.accounts.models import DoctorsModel, AppUserModel
from doc_log.doc_log_app.models import DoctorReviewModel


class CreateDoctorView(views.CreateView):
    form_class = DoctorRegistrationForm
    template_name = 'account/create_doctor.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('home')


class EditDoctorView(views.UpdateView):
    model = DoctorsModel
    form_class = DoctorEditForm
    template_name = 'account/edit_doctor.html'

    def get_success_url(self):
        return reverse('doctor details', kwargs={'pk': self.kwargs.get('pk')})


class DoctorDetailView(views.DetailView):
    model = DoctorsModel
    template_name = 'account/doctor_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = DoctorsModel
        owner = self.object.user_id == self.request.user.id
        # reviews = DoctorReviewModel.objects.filter(doctor=self.object.user_id).distinct()
        rating = DoctorReviewModel.objects.filter(doctor=self.object.user_id).distinct().annotate(
            sum=Sum('rating')).aggregate(Avg('sum'))  # I want to make this better with less SELECTS!!!!!!
        # rating = reviews.annotate(sum=Sum('rating')).aggregate(Avg('sum'))
        # I want to make this better with less SELECTS!!!!!!
        activities = self.get_related_activities()  # (reviews)

        context.update({
            'model': model,
            'is_owner': owner,
            # 'reviews': reviews,
            'rating': rating["sum__avg"],
            'page_obj': activities,

        })
        return context

    def get_related_activities(self):  # , reviews):
        queryset = DoctorReviewModel.objects.filter(
            doctor=self.object.user_id).distinct()  # I want to make this better with less SELECTS!!!!!!
        # queryset = reviews # I want to make this better with less SELECTS!!!!!!
        paginator = Paginator(queryset, 3)
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities


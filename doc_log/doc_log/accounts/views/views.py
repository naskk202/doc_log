from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from doc_log.accounts.forms import DeleteUserForm
from doc_log.accounts.models import AppUserModel


class UserLoginView(auth_views.LoginView):
    template_name = 'account/login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class DeleteUserView(views.DeleteView):
    model = AppUserModel
    form_class = DeleteUserForm
    template_name = 'account/delete_user.html'
    success_url = reverse_lazy('home')


class ChangePasswordView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'account/change_password.html'


def logout_view(request):
    logout(request)
    return redirect('home')

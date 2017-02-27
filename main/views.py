from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ExtendedUser
from . import forms


class IndexView(LoginRequiredMixin, generic.DetailView):
    template_name = 'user.html'
    model = ExtendedUser
    login_url = '/login/'
    redirect_field_name = ''


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm
    # success_url = '/login_act/'


def login_act(request):
    try:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['id'] = user.id
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('user_page', args=(request.user.id,)))
        else:
            return HttpResponseRedirect(reverse_lazy('login_page'))
    except:
        return HttpResponseRedirect(reverse_lazy('login_page'))


def logout_act(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login_page'))


class RegistrationView(generic.FormView):
    template_name = 'registration.html'
    form_class = forms.RegistrationForm


def registration_act(request):
    try:
        if request.POST['password'] == request.POST['confirm_password']:
            new_user = ExtendedUser(
                username=request.POST['username'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            new_user.set_password(request.POST['password'])
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('user_page', args=(new_user.id,)))
        else:
            return HttpResponseRedirect(reverse_lazy('registration_view'))
    except:
        return HttpResponseRedirect(reverse_lazy('registration_view'))

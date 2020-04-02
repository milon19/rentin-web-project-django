from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'


def Register(request):
    return render(request, 'users/register.html')
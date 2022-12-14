from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from accounts.forms import UserRegisterForm


class MySignupView(CreateView):
    """Регистрация"""
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class MyLoginView(LoginView):
    """Вход в аккаунт"""
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


class MyLogoutView(LogoutView):
    """Выход из аккаунта"""
    success_url = reverse_lazy('geo:index')

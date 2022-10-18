from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'geo_app/index.html'


class PrivateRoomView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/private_room.html'


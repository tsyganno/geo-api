from dadata import Dadata

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'geo_app/index.html'


class PrivateRoomView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/private_room.html'


class ParsingCitiesView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/parsing_cities.html'


def process_parsing(request):
    token = "180d4258a7350e2d2e7aa62d1c31d1f57d24575a"
    secret = "18ac391b58a8c17b578a20e753c1b79d1926915f"
    dadata = Dadata(token, secret)
    result = dadata.clean("address", "Алтайский край, г Белокуриха,659900,Россия,Сибирский,край,Алтайский,,,город,Белокуриха,,,2200000300000,e4edca96-9b86-4cac-8c7f-cc93d9ba4cd1,4,0,1404000000,1704000001,2204,UTC+7,51.996152,84.9839604,15072,1846")
    for key in result.keys():
        print(key, result[key])

    return HttpResponseRedirect(reverse('geo:ending_parsing'))


class EndingParsingView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/ending_parsing.html'

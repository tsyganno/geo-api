from dadata import Dadata
from django.views.generic import CreateView

from .forms import MyModelForm
from .models import MyModel

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from geo_app.models import City


class MyCreateView(CreateView):
    form_class = MyModelForm
    model = MyModel

    def get_success_url(self):
        return reverse("geo:form")


class IndexView(TemplateView):
    template_name = 'geo_app/index.html'


class PrivateRoomView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/private_room.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8)
    #     map.save("geo_app/private_room.html")
    #     return context


class ParsingCitiesView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/parsing_cities.html'


def process_parsing(request):
    count = 0
    city_element = City()
    token = "180d4258a7350e2d2e7aa62d1c31d1f57d24575a"
    secret = "18ac391b58a8c17b578a20e753c1b79d1926915f"
    dadata = Dadata(token, secret)
    with open('cities/city.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.split(','))
            print()
            # result = dadata.clean("address", line.strip())
            # city_element.country = result['country']
            # city_element.federal_district = result['federal_district']
            # city_element.region = result['region']
            # city_element.city = result['city']
            # city_element.street = result['street']
            # city_element.house = result['house']
            # city_element.block = result['block']
            # city_element.flat = result['flat']
            # city_element.geo_lat = result['geo_lat']
            # city_element.geo_lon = result['geo_lon']
            # city_element.save()
            count += 1
    print(count)
    return HttpResponseRedirect(reverse('geo:ending_parsing'))


class EndingParsingView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/ending_parsing.html'

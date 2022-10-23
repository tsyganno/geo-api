from dadata import Dadata
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django_admin_geomap import geomap_context

from geo_app.models import MyModel
from geo_app.forms import MyModelForm, LocationlForm


def found_city(request):
    if request.method == "POST":
        title = str(request.POST['location']).title()
        id_user = request.user.pk
        location = MyModel.objects.filter(location=title, user__id=id_user)
        return render(request, 'geo_app/found_city.html', geomap_context(location, auto_zoom="10"))
    else:
        return render(request, 'geo_app/found_city.html')


class CitySearchView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/city_search.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/private_room.html'

    def get_context_data(self, **kwargs):
        return geomap_context(MyModel.objects.filter(user__id=self.request.user.pk), auto_zoom="10")


class MyCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    form_class = MyModelForm
    model = MyModel

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("geo:add_location")


class IndexView(TemplateView):
    template_name = 'geo_app/index.html'


class ParsingCitiesView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/parsing_cities.html'


def process_parsing(request):
    counter = 0
    with open('cities/city.csv', 'r', encoding='utf-8') as file:
        for line in file:
            counter += 1
    data = MyModel.objects.filter(user__id=request.user.pk)
    message = 'Города из файла уже распарсены, БД заполнена.'
    if len(data) > counter - 2:
        return render(request, 'geo_app/ending_parsing.html', {'message': message})
    count = 0
    # token = "180d4258a7350e2d2e7aa62d1c31d1f57d24575a"
    # secret = "18ac391b58a8c17b578a20e753c1b79d1926915f"
    # dadata = Dadata(token, secret)
    with open('cities/city.csv', 'r', encoding='utf-8') as file:
        for line in file:
            element = []
            array_city = line.strip().split(',')
            for i in range(len(array_city)):
                if array_city[i].strip().lower() == 'город':
                    element.append(array_city[i + 1])
                elif '.' in array_city[i] and (array_city[i].strip()[:array_city[i].find('.')] + array_city[i].strip()[array_city[i].find('.') + 1:]).isdigit():
                    element.append(array_city[i])
            if count > 0:
                city_element = MyModel()
                city_element.location = element[0]
                city_element.latitude = element[-2]
                city_element.longitude = element[-1]
                city_element.user = request.user
                city_element.save()

            # result = dadata.clean("address", line.strip())
            # city_element.country = result['country']
            # city_element.federal_district = result['federal_district']
            # city_element.region = result['region']
            # city_element.location = result['city']
            # city_element.street = result['street']
            # city_element.house = result['house']
            # city_element.block = result['block']
            # city_element.flat = result['flat']
            # city_element.latitude = result['geo_lat']
            # city_element.longitude = result['geo_lon']
            # city_element.save()
            count += 1
    # dadata.close()
    return HttpResponseRedirect(reverse('geo:ending_parsing'))


class EndingParsingView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    template_name = 'geo_app/ending_parsing.html'


class DeleteLocationView(LoginRequiredMixin, DeleteView):
    login_url = 'accounts:login'
    template_name = 'geo_app/delete_location.html'
    model = MyModel

    def get_queryset(self):
        owner = self.request.user.pk
        return self.model.objects.filter(user__id=owner)

    def get_object(self, queryset=None):
        return self.get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['location'] = MyModel.objects.filter(user__id=self.request.user.pk)
        return context

    def get_success_url(self):
        return reverse('geo:private_room')

from django.urls import path
from geo_app.views import IndexView, ParsingCitiesView, process_parsing, EndingParsingView, MyCreateView, \
    CitySearchView, HomeView, found_city, DeleteLocationView

app_name = 'geo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('private_room/', HomeView.as_view(), name='private_room'),
    path('private_room/add_location/', MyCreateView.as_view(), name='add_location'),
    path('private_room/parsing_cities/', ParsingCitiesView.as_view(), name='parsing_cities'),
    path('private_room/parsing_cities/process_parsing', process_parsing, name='process_parsing'),
    path('private_room/parsing_cities/ending_parsing', EndingParsingView.as_view(), name='ending_parsing'),
    path('private_room/city_search/', CitySearchView.as_view(), name='city_search'),
    path('private_room/city_search/found_city/', found_city, name='found_city'),

    path('private_room/delete_location/', DeleteLocationView.as_view(), name='delete_location'),
]

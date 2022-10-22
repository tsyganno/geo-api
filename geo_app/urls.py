from django.urls import path
from geo_app.views import IndexView, ParsingCitiesView, process_parsing, EndingParsingView, MyCreateView, home

app_name = 'geo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('private_room/', home, name='private_room'),
    path('add_location/', MyCreateView.as_view(), name='add_location'),
    path('private_room/parsing_cities/', ParsingCitiesView.as_view(), name='parsing_cities'),
    path('private_room/parsing_cities/process_parsing', process_parsing, name='process_parsing'),
    path('private_room/parsing_cities/ending_parsing', EndingParsingView.as_view(), name='ending_parsing'),
]

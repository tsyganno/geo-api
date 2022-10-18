from django.urls import path
from geo_app.views import IndexView

app_name = 'geo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

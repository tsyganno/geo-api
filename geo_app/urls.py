from django.urls import path
from geo_app.views import IndexView, PrivateRoomView

app_name = 'geo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('private_room/', PrivateRoomView.as_view(), name='private_room'),
]

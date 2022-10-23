from django import forms
from geo_app.models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        fields = ('location', 'latitude', 'longitude',)
        model = MyModel

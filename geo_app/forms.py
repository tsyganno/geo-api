from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from geo_app.models import MyModel


class LocationlForm(forms.ModelForm):

    class Meta:
        fields = ('location', )
        model = MyModel


class MyModelForm(forms.ModelForm):

    class Meta:
        fields = ('location', 'latitude', 'longitude', )
        model = MyModel


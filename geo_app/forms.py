from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import MyModel


class MyModelForm(forms.ModelForm):

    class Meta:
        fields = ('location', 'latitude', 'longitude', )
        model = MyModel

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'location',
                'latitude',
                'longitude',
            ),
            ButtonHolder(Submit('submit', 'Сохранить'))
        )
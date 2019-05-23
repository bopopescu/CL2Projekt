
from .models import  Turnament
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime


class AddForm(forms.Form):
    name = forms.CharField()
    place = forms.CharField()
    description= forms.CharField()
    date_start = forms.DateField(input_formats=['%Y-%m-%d'], initial=datetime.date.today)
    date_end = forms.DateField(input_formats=['%Y-%m-%d'])
    price = forms.IntegerField()

    class Meta():
        model = Turnament
        fields = ('Nazwa Turnieju', 'Miejsce', 'Poczatek', 'Koniec',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="wpisz poprawny email")



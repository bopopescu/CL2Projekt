from .models import  Turnament
from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime


class AddForm(forms.Form):
    name = forms.CharField()
    place = forms.CharField()
    description= forms.CharField()
    date_start = forms.DateField(
    widget=forms.SelectDateWidget)
    date_end = forms.DateField(
    widget=forms.SelectDateWidget)
    price = forms.IntegerField()

    class Meta():
        model = Turnament
        fields = ('Nazwa Turnieju', 'Miejsce', 'Poczatek', 'Koniec',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="wpisz poprawny email")



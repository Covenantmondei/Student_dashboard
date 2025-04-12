from django.forms import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):
    password = forms.
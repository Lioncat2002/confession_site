from dataclasses import fields
from django.forms import ModelForm
from .models import Confessions

class ConfessionForm(ModelForm):
    class Meta:
        model=Confessions
        fields='__all__'
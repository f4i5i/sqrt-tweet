from django import forms
from .models import *


class FbProfileForm(forms.ModelForm):

    class Meta:
        model = FbProfile
        fields = "__all__"
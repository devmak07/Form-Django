from django import forms
from .models import *

class formdata(forms.ModelForm):
    #file = forms.FileField(widget=forms.ClearableFileInput())
    class Meta:
        model=form_detail
        fields='__all__'
    
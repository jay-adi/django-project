from .models import upi
from django import forms


class Formm1(forms.ModelForm):
    class Meta:
        model=upi
        fields=('name','email','transid')
        #fields="__all__"
        # exclude=['title']
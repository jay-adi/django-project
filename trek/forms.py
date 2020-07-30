from .models import Product,upi
from django import forms


class Formm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','height','weight','address','trek','couponcode','id_proof')
        #fields="__all__"
        # exclude=['title']
class Formm1(forms.ModelForm):
    class Meta:
        model=upi
        fields=('upiname','email','transid')
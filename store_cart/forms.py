from django import forms
from django.forms.fields import BooleanField

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]



class AddProductToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

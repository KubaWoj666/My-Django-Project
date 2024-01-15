from django import forms

from .models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["price"]

    
class SaleSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

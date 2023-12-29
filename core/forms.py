from django import forms

from .models import Item

class ItemEditForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Item
        # fields = ["image", "inside_number", "name", ]
        exclude = ["id" ]
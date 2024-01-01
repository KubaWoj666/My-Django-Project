from django import forms

from .models import Item, Category

class ItemEditForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Item
        # fields = ["image", "inside_number", "name", ]
        exclude = ["id" ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
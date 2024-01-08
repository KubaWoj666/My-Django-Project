from django import forms

from .models import Item, Category

class ItemEditForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Item
        # fields = ["image", "inside_number", "name", ]
        exclude = ["id" ]


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={"placeholder": "Enter a new category"}))
    class Meta:
        model = Category
        fields = ["category_name"]



FORMAT_CHOICE = (
    ("xls", "xls"),
)
class FormatForm(forms.Form):
    format = forms.ChoiceField(choices=FORMAT_CHOICE, widget=forms.Select(attrs={"class": "form-select"}))
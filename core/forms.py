from django import forms

from .models import Item, Category, MainCategory

class ItemEditForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    # main_category = forms.ModelChoiceField(queryset=MainCategory.objects.all(), label="Main category")
    class Meta:
        model = Item
        # fields = ["image", "inside_number", "name", ]
        exclude = ["id" ]


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={"placeholder": "Enter a new category"}))
    class Meta:
        model = Category
        fields = ["category_name", "main_cat_name"]

class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    main_category = forms.ModelChoiceField(queryset=MainCategory.objects.all(), required=False, label='Main Category')





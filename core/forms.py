from django import forms

from .models import Item, Category, MainCategory, Image, MetalPrice

class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["id"]

    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget.attrs.update({'class': 'form-control border-primary', 'multiple': True})

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

class MetalPriceForm(forms.ModelForm):
    weight = forms.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = MetalPrice
        fields = ['weight', 'grade']
    


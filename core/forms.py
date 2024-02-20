from django import forms

from .models import Item, Category, MainCategory, Image

class ItemEditForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Item
        exclude = ["id"]

    # function for adding "multiple" arguments form control
    # this is needed if you wont send more than one photo to form
    # def __init__(self, *args, **kwargs):
    #     super(ItemEditForm, self).__init__(*args, **kwargs)
    #     self.fields["image"].widget.attrs.update({'class': 'form-control border-primary', 'multiple': True})
    
class ImageForm(forms.ModelForm):
    # image = forms.ImageField(
    #     label="Images", widget=forms.FileInput)
        

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





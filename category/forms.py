from django import forms
from .models import Category
class create_categoForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('category_name', 'description', 'cat_image')
        
        
        category_name = forms.CharField(
                max_length=70,
                label="nom",
                help_text="Write post title here. The title must be have max 70 characters",
                widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                )
        
        slug = forms.SlugField(
                    max_length=70,
                    label="Slug",
                    help_text="Slug is a field in autocomplete mode, but if you want you can modify its contents",
                    widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
                    )
        
    def __init__(self, *args, **kwargs):
        super(create_categoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
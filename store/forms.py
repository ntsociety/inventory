from django import forms
from .models import AddStocks, Product, Supplier, Customer
from category.models import Category



#supplier
class supplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('first_name', 'last_name', 'phone', 'address', 'email', 'image_profil' )
    
    def __init__(self, *args, **kwargs):
        super(supplierForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
        
#product        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'images', 'stock_initial', 'category', 'supplier')
        
        
        
    product_name = forms.CharField(label='Nom',
                                   required=True, 
                                   widget=forms.TextInput(attrs={
        "placeholder": "Nom",
        "class": "form-control"
        }))
    
    
    
    
   
    
    description = forms.CharField(label='Description',
                                  required=False,
                                  widget=forms.TextInput(attrs={
        "placeholder": "Description",
        "class": "form-control"
        }))
    price = forms.IntegerField(label='Prix', required=True,)
    stock_initial = forms.IntegerField(label='Stock iniatial', required=True,)
    images = forms.ImageField(label='Image', required=False,)
    # category = forms.ModelChoiceField(label='categorie',
    #                                   queryset=Category.objects.all(), 
    #                                   required=False,)
    # supplier = forms.ModelChoiceField(label='Fournisseur', 
    #                                 queryset=Supplier.objects.all(),
    #                                 required=False,)
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs['placeholder'] = 'name'
        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter prix'
        self.fields['images'].widget.attrs['placeholder'] = 'images'
        self.fields['stock_initial'].widget.attrs['placeholder'] = 'stock initial'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    # def __init__(self, user, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['category'].queryset=Category.objects.filter(user=user)
    
    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset=Supplier.objects.filter(user=user)
        self.fields['category'].queryset=Category.objects.filter(user=user)
            
    
    
#add stock
class Add_stockForm(forms.ModelForm):
    
    class Meta:
        model = AddStocks
        fields = ('product', 'quantity')
        
        
    def __init__(self, *args, **kwargs):
        super(Add_stockForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['placeholder'] = 'product'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter quantity'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

#customer
class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone', 'address', 'email', 'image_profil' )
    
    def __init__(self, *args, **kwargs):
        super(customerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
            
        
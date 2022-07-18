from django import forms
from .models import Order
from store.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'product', 'quantity', 'status')
        
   
   
    # product = forms.CharField(label='',
    #                                required=True, 
    #                                 widget=forms.ModelMultipleChoiceField(queryset=None,))
    
    
    # product = forms.CharField(label='',
    #                               required=False,
    #                               widget=forms.TextInput(attrs={
    #                                   "type":"text",
    #     "list": "citylist",
    #     "placeholder": "Description",
    #     "class": "form-control",
    #     "id": "citylist",
    #     }))
    
    
    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['product'].queryset = Product.objects.filter(product_name__contains='W')
       
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs['placeholder'] = 'customer'
        self.fields['product'].widget.attrs['placeholder'] = 'product'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter quantity'
        self.fields['status'].widget.attrs['placeholder'] = 'status'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    
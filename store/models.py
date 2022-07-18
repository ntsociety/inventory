from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Supplier(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image_profil = models.ImageField(upload_to='photos/fournisseur', blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return self.first_name
    
    
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    description     = models.CharField(max_length=500, blank=True, null=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products', blank=True, null=True)
    stock           = models.IntegerField(blank=True, default=0, null=True)
    stock_initial           = models.IntegerField(default=0,)
    stock_final           = models.IntegerField(blank=True, default=0, null=True)
    sell           = models.IntegerField(default=0, blank=True)
    add_stock           = models.IntegerField(blank=True, default=0, null=True)
    variation           = models.IntegerField(default=0, null=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    supplier        = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    # def save(self, *args, **kwargs):
    #     self.tags = self.product_name + '' + self.slug
    #     super(Product, self).save(*args, **kwargs)
    
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        
    
    def prix_sell(self):
        prix_sell = 0
        if self.sell:
            prix_sell= self.sell * self.price
        return prix_sell
    
    
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])
   
    
    def __str__(self):
        return self.product_name
    
    
    
    
    


class AddStocks(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.product.product_name
    
    
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image_profil = models.ImageField(upload_to='photos/client', blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.first_name
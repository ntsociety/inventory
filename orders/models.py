
from django.db import models
from store.models import Product, Customer
# Create your models here.


STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='created')
    quantity = models.IntegerField()
    sub_total = models.IntegerField(null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    
    # def sub_total(self):
    #     return self.product.price * self.quantity
    
    # def vente(self):
    #     vente = 0
    #     if self.quantity:
    #         vente = self.quantity
    #     return vente
    
    
    # def prix_unit(self):
    #     prix_unit = 0
    #     if self.product:
    #         prix_unit = self.product.price
    #     return prix_unit
        
        
    # def stock_final(self):
    #     stock_final = 0
    #     if self.product:
    #         stock_final = self.product.stock - self.quantity
    #     return stock_final    
    
    
    def sub_total(self):
        sub_total = 0
        if self.product:
            sub_total = self.product.price * self.quantity
        return sub_total
    
    # def stock_restant(self):
    #     stock_restant = 0
    #     if self.product:
    #         stock_restant = self.product.stock - self.quantity
    #     return stock_restant
    
    def __str__(self):
        return self.product.product_name
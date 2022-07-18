from django.contrib import admin
from store.models import AddStocks, Product, Supplier, Customer
from import_export.admin import ExportActionMixin
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.images.url))
    thumbnail.short_description = 'images'
    list_display = ('product_name', 'price', 'stock_initial', 'stock', 'add_stock', 'category', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    
    
class AddStockAdmin(admin.ModelAdmin):
    list_display = ('product','created_date')
    
    
admin.site.register(Product, ProductAdmin)



admin.site.register(Supplier)



admin.site.register(Customer)

admin.site.register(AddStocks, AddStockAdmin)
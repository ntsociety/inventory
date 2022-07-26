from . import views
from django.urls import path


urlpatterns = [
    #partie supplier
    path('supplier/create_supplier', views.create_supplier, name='create_supplier'),
    path('supplier/supplier', views.supplier, name='supplier'),
    path('supplier/supplier_detail/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('supplier/edit_supplier/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('supplier/supplier_delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
    path('search_supplier', views.search_supplier, name='search_supplier'),
    
    #partie customer
    path('customer/create_customer', views.create_customer, name='create_customer'),
    path('customer/customer', views.customer, name='customer'),
    path('customer/customer_detail/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/edit_customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customer/customer_delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('search_customer', views.search_customer, name='search_customer'),
    
    
    #search
    path('search', views.search, name='search'),
    
    #partie produit
    path('', views.product, name='product'),
    path('category/<slug:category_slug>/', views.product, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('add_quantity', views.add_quantity, name='add_quantity'),
    path('create_product', views.create_product, name='create_product'),
    path('products_detail/<int:pk>/', views.product_detail, name='products_detail'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('product_delete/<int:pk>/', views.product_delete, name='product_delete'),
    
    
    #excel data export
    path('export_data_product', views.export_data_product, name='export_data_product')
    
   
    
]

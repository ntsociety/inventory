from . import views
#from .views import OrderListView
from django.urls import path


urlpatterns = [
    #path('order/', OrderListView.as_view(), name='order'),
    path('', views.order, name='order'),
    path('add_cart/', views.addCart, name='addCart'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('edit_order/<int:pk>/', views.edit_order, name='edit_order'),
    path('order_delete/<int:pk>/', views.order_delete, name='order_delete'),
    
    #  #search
    path('search_order', views.search_order, name='search_order'),
    
    #excel data export
    path('export_data_order', views.export_data_order, name='export_data_order')
    
]

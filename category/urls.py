from . import views
from django.urls import path


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create_catego/', views.create_catego, name='create_catego'),
    path('edit_catego/<int:pk>/', views.edit_catego, name='edit_catego'),
    path('detail_catego/<int:pk>/', views.detail_catego, name='detail_catego'),
    path('catego_delete/<int:pk>/', views.catego_delete, name='catego_delete'),
]

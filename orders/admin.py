from django.contrib import admin
from .models import Order
from import_export.admin import ExportActionMixin
# Register your models here.

class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('product', 'quantity', 'sub_total', 'customer', 'status')


admin.site.register(Order, OrderAdmin)
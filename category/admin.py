from django.contrib import admin
from .models import Category

from django.utils.html import format_html
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.cat_image.url))
    thumbnail.short_description = 'cat_image'
    prepopulated_fields = {'slug': ('category_name',)}
    #list_display = ('thumbnail', 'category_name', 'slug')

admin.site.register(Category, CategoryAdmin)

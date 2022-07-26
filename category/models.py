from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.tags = self.category_name + '' + self.slug
        super(Category, self).save(*args, **kwargs)
    
    
    
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.category_name)
    #     super(Category, self).save(*args, **kwargs)
    
    
    
        
        
        

        
    def __str__(self):
        return self.category_name
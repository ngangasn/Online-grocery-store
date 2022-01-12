from django.db import models
from django.urls.base import reverse
from accounts.customer import Customer


class Category(models.Model):
    category_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ('category_name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("shop:products_sorted_with_category", kwargs={"category_slug": self.slug})
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('product_name', )
        index_together = (('id', 'slug'), )
    
    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"id": self.id, "product_slug": self.slug})
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

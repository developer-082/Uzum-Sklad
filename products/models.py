from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique = True)
    category = models.CharField(max_length=100)
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.CASCADE, related_name='products')
    stock = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_stock = models.IntegerField(default = 10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def is_low_stock(self):
        return self.stock <= self.min_stock

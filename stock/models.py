from django.db import models
from django.core.exceptions import ValidationError
from products.models import Product
from suppliers.models import Supplier

# Create your models here.
class Stock_in(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_ins')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='stock_ins')
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Stock in: {self.product.name} - {self.quantity}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.product.stock += self.quantity
            self.product.save()
        super().save(*args, **kwargs)

class Stock_out(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_outs')
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stock out: {self.product.name} {self.quantity}"
    
    def clean(self):
        if self.product.stock < self.quantity:
            raise ValidationError("Omborda yetarlicha narsa yo'q")
    
    def save(self, *args, **kwargs):
        self.clean()

        if not self.pk:
            self.product.stock -= self.quantity
            self.product.save()
        
        super().save(*args, **kwargs)
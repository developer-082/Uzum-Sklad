from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=150)
    address = models.TextField(max_length=150)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.company}"
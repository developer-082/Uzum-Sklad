from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'category',
            'supplier',
            'price',
            'min_stock'
        ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'sku':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'min_stock':forms.NumberInput(attrs={'class':'form-control'})
        }
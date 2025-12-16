from django import forms
from .models import Stock_in, Stock_out

class StockInForm(forms.ModelForm):
    class Meta:
        model = Stock_in
        fields = [
            'product',
            'supplier',
            'quantity',
            'purchase_price'
        ]
        widgets = {
            'product':forms.Select(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'purchase_price':forms.NumberInput(attrs={'class':'form-control'}),
        }

class StockOutForm(forms.ModelForm):
    class Meta:
        model = Stock_out
        fields = [
            'product',
            'quantity',
            'customer_name'
        ]
        widgets = {
            'product':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'customer_name':forms.TextInput(attrs={'class':'form-control'}),
        }

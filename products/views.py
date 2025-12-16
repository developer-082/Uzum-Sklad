from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from stock.models import Stock_in, Stock_out
from suppliers.models import Supplier
from django.utils import timezone
from .forms import ProductForm
from django.db.models import F, Sum
from .models import Product

@login_required
def dashboard(request):
    total_products = str(Product.objects.count()) + " ta"
    total_suppliers = str(Supplier.objects.count()) + " ta"

    today = timezone.now().date()

    today_stock_in = str(Stock_in.objects.filter(created_at__date=today).aggregate(total_sum = Sum(F('quantity')*F('purchase_price')))['total_sum'] or 0) + " so'm"

    today_stock_out = str(Stock_out.objects.filter(created_at__date=today).aggregate(total_sum = Sum(F('quantity')*F('product__price')))['total_sum'] or 0) + " so'm"

    low_stock_products = Product.objects.filter(stock__lte = F('min_stock'))

    context = {
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'today_stock_in': today_stock_out,
        'today_stock_out': today_stock_in,
        'low_stock_products': low_stock_products,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Mahsulot qo\'shish'})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Mahsulotni tahrirlash'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

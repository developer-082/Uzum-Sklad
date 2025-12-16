from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Stock_in, Stock_out
from suppliers.models import Supplier
from django.utils import timezone
from datetime import timedelta
from .forms import StockInForm, StockOutForm
from django.db.models import F, Sum

@login_required
def stock_in_list(request):
    stock_ins = Stock_in.objects.all().order_by('-created_at')
    return render(request, 'stock/stock_in_list.html', {'stock_ins': stock_ins})

@login_required
def stock_in_create(request):
    if request.method == 'POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_in_list')
    else:
        form = StockInForm()
    return render(request, 'stock/stock_form.html', {'form': form, 'title': 'Omborga kiritish'})

@login_required
def stock_out_list(request):
    stock_outs = Stock_out.objects.all().order_by('-created_at')
    return render(request, 'stock/stock_out_list.html', {'stock_outs': stock_outs})

@login_required
def stock_out_create(request):
    if request.method == 'POST':
        form = StockOutForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('stock_out_list')
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = StockOutForm()
    return render(request, 'stock/stock_form.html', {'form': form, 'title': 'Ombordan olish'})

@login_required
def statistika(request):
    hafta = timezone.now() - timedelta(days = 7)
    print(hafta)
    haftalik_kirimlar = (Stock_in.objects.filter(created_at__gte = hafta).aggregate(total = Sum(F('quantity') * F('purchase_price')))['total'])
    haftalik_chiqimlar = (Stock_out.objects.filter(created_at__gte = hafta).aggregate(total = Sum(F('quantity') * F('product__price')))['total'])
    
    foyda = haftalik_chiqimlar - haftalik_kirimlar

    eng_kop_sotilgan = Stock_out.objects.filter(created_at__gte = hafta).order_by('quantity')[:5]

    suppliers = Supplier.objects.annotate(soni = F('stock_ins')).order_by('soni')[:5]

    context ={
        'kirimlar': haftalik_chiqimlar,
        'chiqimlar': haftalik_kirimlar,
        'foyda': foyda,
        'top_sotilgan': eng_kop_sotilgan,
        'top_suppliers': suppliers,
    }
    return render(request, 'statistics.html', context = context)

"""
URL configuration for uzum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from products.views import dashboard
from django.urls import path
from django.contrib.auth import views as auth_views
from suppliers.views import supplier_list, supplier_create
from stock.views import stock_in_list, stock_in_create, stock_out_list, stock_out_create, statistika
from products.views import dashboard, product_list, product_create, product_edit, product_delete
from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name = 'dashboard')
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # productlar
    path('products/', product_list, name='product_list'),
    path('products/add/', product_create, name='product_create'),
    path('products/edit/<int:pk>/', product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),

    # suppliers
    path('suppliers/', supplier_list, name='supplier_list'),
    path('suppliers/add/', supplier_create, name='supplier_create'),

    # stovk amalllari
    path('stock-in/', stock_in_list, name='stock_in_list'),
    path('stock-in/add/', stock_in_create, name='stock_in_create'),
    path('stock-out/', stock_out_list, name='stock_out_list'),
    path('stock-out/add/', stock_out_create, name='stock_out_create'),
    path('statistics/', statistika, name='statistics'),

    # logini
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login')
]

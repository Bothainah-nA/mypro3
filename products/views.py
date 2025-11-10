from django.shortcuts import render
from .models import Product  # لجلب المنتجات من قاعدة البيانات

def home(request):
    """
    الصفحة الرئيسية تعرض البنر + بعض المنتجات
    """
    products = Product.objects.filter(is_available=True).order_by('-created_at')[:6]  # نعرض آخر 6 منتجات
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)


def products_list(request):
    """
    صفحة المنتجات الكاملة
    """
    products = Product.objects.filter(is_available=True).order_by('-created_at')
    context = {
        'products': products,
    }
    return render(request, 'products-templates/products_list.html', context)

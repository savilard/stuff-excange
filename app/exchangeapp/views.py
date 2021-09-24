from django.shortcuts import render


def add_product(request):
    return render(request, 'add_product.html')


def all_products(request):
    return render(request, 'all_products.html')
from django.shortcuts import render


def add_product(request):
    return render(request, 'add_product.html')

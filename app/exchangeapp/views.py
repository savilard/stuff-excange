from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Product

ITEMS_PER_PAGE = 9


def add_product(request):
    return render(request, 'product/add_product.html')


def all_products(request):
    products = Product.objects.all()
    products_amount = products.count()

    paginator = Paginator(products, ITEMS_PER_PAGE)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'product/all_products.html',
        {
            'products': products,
            'products_amount': products_amount,
            'page_object': page,
            'paginator': paginator,
        }
    )

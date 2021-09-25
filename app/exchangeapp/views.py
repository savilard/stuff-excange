from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .forms import ProductForm, ProductImageFormSet
from .models import Product

ITEMS_PER_PAGE = 9


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductAddView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['images'] = ProductImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['images'] = ProductImageFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object
            images.save()
        else:
            return self.form_invalid(form)
        return super(ProductAddView, self).form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


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

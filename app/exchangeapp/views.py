from django.views.generic import CreateView, DetailView, ListView

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

        product_instance = form.save(commit=False)
        product_instance.owner = self.request.user
        product_instance.save()

        if images.is_valid():
            product_instance = form.save()
            images.instance = product_instance
            images.save()

        else:
            return self.form_invalid(form)
        return super(ProductAddView, self).form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


class ProductsDisplayAllView(ListView):
    model = Product
    template_name = 'product/all_products.html'
    paginate_by = ITEMS_PER_PAGE

    def get_context_data(self, **kwargs):
        user_products = self.get_queryset()
        context = {
            'products_amount': user_products.count(),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class UserProductsView(ListView):
    model = Product
    template_name = 'product/user_products.html'
    paginate_by = ITEMS_PER_PAGE

    def get_context_data(self, **kwargs):
        user_products = self.get_queryset()
        context = {
            'products_amount': user_products.count(),
            'owner_username': self.kwargs['username'],
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return super(UserProductsView, self).get_queryset().filter(owner__username=self.kwargs['username'])

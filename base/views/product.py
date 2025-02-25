from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView


from base.models.product import Product, ProductCategory, Supplier
from base.forms.product import ProductForm, ProductCategoryForm, SupplierForm
from base.views.common_view import CustomDeleteView


class ProductListView(TemplateView):
    # paginate_by = 20
    # model = Product
    template_name = "product.html"

    def post(self, request, *args, **kwargs):
        form = ProductForm(self.request.POST)
        product_id = request.POST.get('product_id')
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            form = ProductForm(self.request.POST, instance=product)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'data created/updated with the ID:{data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('product-home')
        # return super(ProductListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.all().order_by('pk')
        paginator_products = Paginator(products, 10)
        product_page_number = self.request.GET.get('product_page')
        context['products'] = paginator_products.get_page(product_page_number)

        context['form'] = ProductForm()
        return context


class ProductDelete(CustomDeleteView):
    model = Product
    messages_name = "Product"
    success_url = reverse_lazy('product-home')

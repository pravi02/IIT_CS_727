from django.contrib import messages
from django.core.paginator import Paginator
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
        form = None
        if 'form1' in self.request.POST:
            form = ProductForm(self.request.POST)
        elif 'form2' in self.request.POST:
            form = ProductCategoryForm(self.request.POST)
        elif 'form3' in self.request.POST:
            form = SupplierForm(self.request.POST)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'data created with the ID:{data.pk}')

        return super(ProductListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.all().order_by('pk')
        paginator_products = Paginator(products, 10)
        product_page_number = self.request.GET.get('product_page')
        context['products'] = paginator_products.get_page(product_page_number)

        product_category = ProductCategory.objects.all().order_by('pk')
        paginator_category = Paginator(product_category, 10)
        product_category_page_number = self.request.GET.get('categories_page')
        context['categories'] = paginator_category.get_page(product_category_page_number)

        suppliers = Supplier.objects.all().order_by('pk')
        paginator_supplier = Paginator(suppliers, 10)
        suppliers_page_number = self.request.GET.get('suppliers_page')
        context['suppliers'] = paginator_supplier.get_page(suppliers_page_number)

        context['form1'] = ProductForm()
        context['form2'] = ProductCategoryForm()
        context['form3'] = SupplierForm()
        return context


class ProductDelete(CustomDeleteView):
    model = Product
    messages_name = "Product"
    success_url = reverse_lazy('product-home')

class SupplierDelete(CustomDeleteView):
    model = Supplier
    messages_name = "Supplier"
    success_url = reverse_lazy('product-home')

class ProductCategoryDelete(CustomDeleteView):
    model = ProductCategory
    messages_name = "Product Category"
    success_url = reverse_lazy('product-home')
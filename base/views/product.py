from django.contrib import messages
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
        context['products'] = Product.objects.all().order_by('pk')
        context['categories'] = ProductCategory.objects.all().order_by('pk')
        context['suppliers'] = Supplier.objects.all().order_by('pk')
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
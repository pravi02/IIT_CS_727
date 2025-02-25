from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView


from base.models.product import Product, ProductCategory, Supplier
from base.forms.product import ProductForm, ProductCategoryForm, SupplierForm
from base.views.common_view import CustomDeleteView


class ProductSupplierListView(TemplateView):
    # paginate_by = 20
    # model = Product
    template_name = "supplier.html"

    def post(self, request, *args, **kwargs):

        form = SupplierForm(self.request.POST)
        supplier_id = request.POST.get('supplier_id')
        if supplier_id:
            supplier = get_object_or_404(Supplier, pk=supplier_id)
            form = SupplierForm(self.request.POST, instance=supplier)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'data created/updated with the ID:{data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('product-supplier-home')
        # return super(ProductListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        suppliers = Supplier.objects.all().order_by('pk')
        paginator_supplier = Paginator(suppliers, 10)
        suppliers_page_number = self.request.GET.get('suppliers_page')
        context['suppliers'] = paginator_supplier.get_page(suppliers_page_number)
        context['form'] = SupplierForm()
        return context


class ProductSupplierDelete(CustomDeleteView):
    model = Supplier
    messages_name = "Supplier"
    success_url = reverse_lazy('product-supplier-home')

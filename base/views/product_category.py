from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView


from base.models.product import Product, ProductCategory, Supplier
from base.forms.product import ProductForm, ProductCategoryForm, SupplierForm
from base.views.common_view import CustomDeleteView


class ProductCategoryListView(TemplateView):
    # paginate_by = 20
    # model = Product
    template_name = "product_category.html"

    def post(self, request, *args, **kwargs):
        form = None
        form = ProductCategoryForm(self.request.POST)
        category_id = request.POST.get('category_id')
        if category_id:
            category = get_object_or_404(ProductCategory, pk=category_id)
            form = ProductCategoryForm(self.request.POST, instance=category)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'data created/updated with the ID:{data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('product-category-home')
        # return super(ProductListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_category = ProductCategory.objects.all().order_by('pk')
        paginator_category = Paginator(product_category, 10)
        product_category_page_number = self.request.GET.get('categories_page')
        context['categories'] = paginator_category.get_page(product_category_page_number)
        context['form'] = ProductCategoryForm()
        return context


class ProductCategoryDelete(CustomDeleteView):
    model = ProductCategory
    messages_name = "Product Category"
    success_url = reverse_lazy('product-category-home')
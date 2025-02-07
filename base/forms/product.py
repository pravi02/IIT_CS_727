from django import forms

from base.models.product import Product, Supplier, ProductCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['product_id',]

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['supplier_id',]

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name',]
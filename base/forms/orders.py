from django import forms

from base.models.customer import CustomerOrderItems


class CustomerOrderItemsForm(forms.ModelForm):
    class Meta:
        model = CustomerOrderItems
        fields = ['product', 'request_quantity',]
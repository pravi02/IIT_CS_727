from django import forms

from base.models.product import Product
from base.models.transaction import ProcessedLineItems


class ProcessedLinItemForm(forms.ModelForm):
    class Meta:

        model = ProcessedLineItems
        fields = ["inventory", "allocated_quantity",]

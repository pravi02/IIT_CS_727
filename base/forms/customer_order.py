from django import forms


from base.models.customer import Customer, CustomerOrder, CustomerOrderItems


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder

        fields = ['order_date', 'customer']
        widgets = {
            'order_date': DateInput(),
        }


class CustomerOrderItemsForm(forms.ModelForm):
    class Meta:
        model = CustomerOrderItems
        exclude = ['line_item_id', 'customer_order']
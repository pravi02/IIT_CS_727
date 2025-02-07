from django import forms

from base.models.customer import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_location', 'customer_email', 'customer_telephone']
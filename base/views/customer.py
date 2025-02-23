from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView

from base.forms.customer import CustomerForm
from base.models.customer import Customer
from base.views.common_view import CustomDeleteView


class CustomerListView(TemplateView):

    template_name = "customer.html"

    def post(self, request, *args, **kwargs):
        # Check if it's an update request (if 'customer_id' exists in POST data)
        if 'customer_id' in request.POST:
            customer = get_object_or_404(Customer, pk=request.POST['customer_id'])
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                messages.info(request, f'Customer data successfully updated with the ID: {customer.customer_id}')
            else:
                messages.warning(request, 'Error updating customer. Please check the form.')
        else:  # It's a new customer creation
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'New customer successfully added.')
            else:
                messages.warning(request, 'Error creating customer. Please check the form.')
        return redirect('customer-home')
        # return super(CustomerListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customers = Customer.objects.all().order_by('pk')
        paginator_customers = Paginator(customers, 10)
        customers_page_number = self.request.GET.get('page')
        context['customers'] = paginator_customers.get_page(customers_page_number)
        context['form'] = CustomerForm()
        return context

class CustomerDelete(CustomDeleteView):
    model = Customer
    messages_name = "Customer"
    success_url = reverse_lazy("customer-home")


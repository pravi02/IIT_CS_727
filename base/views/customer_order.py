from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from base.forms.customer_order import CustomerOrderForm, CustomerOrderItemsForm
from base.models.customer import CustomerOrder, CustomerOrderItems
from base.views.common_view import CustomDeleteView

ItemFormSet = formset_factory(CustomerOrderItemsForm, extra=10)

class CustomerOrderListView(TemplateView):
    # paginate_by = 10
    # model = CustomerOrder
    template_name = "orders.html"

    def post(self, request, *args, **kwargs):

        if "item_id"  in request.POST and "form2" in request.POST:
            item = get_object_or_404(CustomerOrderItems, pk=request.POST['item_id'])
            form2 = CustomerOrderItemsForm(self.request.POST, instance=item)
            if form2.is_valid():
                item = form2.save()
                messages.success(request, f'Item data saved at id: {item.pk}')
        else:
            form1 = CustomerOrderForm(self.request.POST)
            formset = ItemFormSet(self.request.POST)
            if form1.is_valid() and formset.is_valid():
                order = form1.save()
                items = formset.save(commit=False)
                order.items.set(items)
                order.save()
                messages.success(request, f'Data saved at id: {order.pk}')
            elif form1.errors:
                for field, errors in form1.errors.items():
                    for error in errors:
                        messages.warning(request, f'{field}: {error}')
        return redirect('orders-home')
        # return super(CustomerOrderListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = CustomerOrder.objects.all().order_by('pk')
        paginator_orders = Paginator(orders, 10)
        inventory_page_number = self.request.GET.get('orders_page')
        context['orders'] = paginator_orders.get_page(inventory_page_number)

        context['form1'] = CustomerOrderForm()
        context['form2'] = CustomerOrderItemsForm()

        return context

class CustomerOrderDelete(CustomDeleteView):
    model = CustomerOrder
    messages_name = "Customer order"
    success_url = reverse_lazy("orders-home")

class CustomerOrderItemDelete(CustomDeleteView):
    model = CustomerOrderItems
    messages_name = "Customer order line item"
    success_url = reverse_lazy("orders-home")
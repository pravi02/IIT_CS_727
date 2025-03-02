from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from base.forms.customer_order import CustomerOrderForm, CustomerOrderItemsForm
from base.forms.transaction import ProcessedLinItemForm
from base.models import ProcessedOrder
from base.models.customer import CustomerOrder, CustomerOrderItems
from base.views.common_view import CustomDeleteView

ItemFormSet = formset_factory(CustomerOrderItemsForm, extra=5)

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
        elif "order_item_id"  in request.POST and "form3" in request.POST:
            item = get_object_or_404(CustomerOrderItems, pk=request.POST['order_item_id'])
            form3 = ProcessedLinItemForm(request.POST)
            processed_order = ProcessedOrder.objects.filter(customer_order=item.customer_order).first()
            if not processed_order:
                processed_order = ProcessedOrder.objects.create(
                    customer_order=item.customer_order,
                )
            if form3.is_valid():
                processed_order.save()
                processed_item = form3.save(commit=False)
                processed_item.process_id = processed_order
                processed_item.customer_order = item.customer_order
                processed_item.customer_line_item = item
                processed_item.save()
                messages.success(request, f'Line Item data processed at id: {item.pk}')
        else:
            form1 = CustomerOrderForm(self.request.POST)
            formset = ItemFormSet(self.request.POST)
            if form1.is_valid() and formset.is_valid():
                order = form1.save()
                for form in formset:
                    if form.cleaned_data:
                        order_item = form.save(commit=False)
                        order_item.customer_order = order  # Assign the order to the order_item
                        order_item.save()
                messages.success(request, f'Successfully created customer order with id: {order.pk}')
            elif form1.errors:
                for field, errors in form1.errors.items():
                    for error in errors:
                        messages.warning(request, f'{field}: {error}')
        return redirect('orders-home')
        # return super(CustomerOrderListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = CustomerOrder.objects.exclude(processedorder__order_processed=True).order_by('pk')

        paginator_orders = Paginator(orders, 10)
        inventory_page_number = self.request.GET.get('orders_page')
        context['orders'] = paginator_orders.get_page(inventory_page_number)
        context['formset'] = ItemFormSet()
        context['form1'] = CustomerOrderForm()
        context['form2'] = CustomerOrderItemsForm()
        context['form3'] = ProcessedLinItemForm()

        return context

class CustomerOrderDelete(CustomDeleteView):
    model = CustomerOrder
    messages_name = "Customer order"
    success_url = reverse_lazy("orders-home")

class CustomerOrderItemDelete(CustomDeleteView):
    model = CustomerOrderItems
    messages_name = "Customer order line item"
    success_url = reverse_lazy("orders-home")
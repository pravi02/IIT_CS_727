from django.core.paginator import Paginator
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from base.forms.customer_order import CustomerOrderForm, CustomerOrderItemsForm
from base.models.customer import CustomerOrder, CustomerOrderItems
from base.views.common_view import CustomDeleteView


class CustomerOrderListView(TemplateView):
    # paginate_by = 10
    # model = CustomerOrder
    template_name = "orders.html"
    ItemFormSet = formset_factory(CustomerOrderItemsForm, extra=10)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.method == "POST":
    #         form1 = CustomerOrderForm(self.request.POST)
    #         form2 = CustomerOrderItemsForm(self.request.POST)
    #         if form1.is_valid() and form2.is_valid():
    #             order = form1.save()
    #             items = form2.cleaned_data["items"]
    #             order.items.set(items)
    #             order.save()
    #
    #     elif self.request.method == "GET":
    #         pass
    #     return queryset

    def post(self, request, *args, **kwargs):
        form1 = CustomerOrderForm(self.request.POST)
        form2 = CustomerOrderItemsForm(self.request.POST)
        if form1.is_valid() and form2.is_valid():
            order = form1.save()
            items = form2.cleaned_data["items"]
            order.items.set(items)
            order.save()
        return super(CustomerOrderListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

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
    messages_name = "Customer Order"
    success_url = reverse_lazy("order-home")
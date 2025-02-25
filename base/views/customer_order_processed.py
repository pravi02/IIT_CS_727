from django.core.paginator import Paginator
from django.views.generic import TemplateView

from base.models import ProcessedOrder

class CustomerOrderProcessedListView(TemplateView):
    template_name = "processed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = ProcessedOrder.objects.filter(order_processed=True).all().order_by('pk')
        paginator_orders = Paginator(orders, 10)
        inventory_page_number = self.request.GET.get('orders_page')
        context['orders'] = paginator_orders.get_page(inventory_page_number)
        return context


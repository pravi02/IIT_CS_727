from django.core.paginator import Paginator
from django.db.models import Sum
from django.views.generic import TemplateView

from base.models import ProcessedOrder
from base.models.transaction import ProcessedLineItems
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class CustomerOrderProcessedListView(TemplateView):
    template_name = "processed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = ProcessedOrder.objects.filter(order_processed=True).all().order_by('pk')
        paginator_orders = Paginator(orders, 10)
        inventory_page_number = self.request.GET.get('page')
        context['orders'] = paginator_orders.get_page(inventory_page_number)
        return context







# def update_processed_status(processed_order):
#     """
#     Updates the processed_status of the associated CustomerOrder to True if all items are fulfilled.
#     Otherwise, it sets the processed_status to False.
#     """
#     # Get the related customer order from the processed order
#     customer_order = processed_order.customer_order
#
#     all_fulfilled = True
#     for order_item in customer_order.order_line_items.all():
#         # Check if there's any order item where allocated quantity is less than requested quantity
#         allocated = ProcessedLineItems.objects.filter(customer_line_item=order_item).aggregate(
#             total_allocated=Sum('allocated_quantity'))['total_allocated'] or 0
#         if allocated < order_item.request_quantity:
#             all_fulfilled = False
#             break
#
#     # Update the order_processed status based on whether all items are fulfilled
#     customer_order.order_processed = all_fulfilled
#     customer_order.save()


# def update_sales_amount(processed_order):
#     """
#     Updates the sales_amount field of the given processed_order based on the allocated quantity
#     of the processed line items and the price of the associated product.
#     """
#     # Calculate the total sales amount for the processed order
#     total_sales_amount = ProcessedLineItems.objects.filter(process_id=processed_order) \
#                              .select_related('inventory__product') \
#                              .aggregate(total=Sum('allocated_quantity' * 'inventory__product__price'))['total'] or 0
#
#     # Update the sales_amount on the ProcessedOrder
#     processed_order.sales_amount = total_sales_amount
#     processed_order.save()

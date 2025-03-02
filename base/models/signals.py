from decimal import Decimal

from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from base.models.transaction import ProcessedLineItems, ProcessedOrder
from base.models.inventory import Inventory


@receiver([post_save, post_delete], sender=ProcessedLineItems)
def update_sales_amount(sender, instance, **kwargs):
    # Calculate the sales amount based on the inventory price and allocated quantity
    product = instance.inventory.product
    allocated_quantity = instance.allocated_quantity
    sales_amount = product.price_per_unit  * allocated_quantity

    # Update the sales_amount in the associated ProcessedOrder
    processed_order = instance.process_id
    processed_order.sales_amount = Decimal(processed_order.sales_amount) + sales_amount
    processed_order.save()

@receiver(post_save, sender=ProcessedLineItems)
def update_processed_status(sender, instance, **kwargs):
    """
    Updates the processed_status of the associated CustomerOrder to True if all items are fulfilled.
    Otherwise, sets the processed_status to False.
    """
    # Get the related customer order from the processed line item
    customer_order = instance.process_id.customer_order


    all_fulfilled = True
    for order_item in customer_order.order_line_items.all():
        # Calculate the total allocated quantity for the order item
        allocated = ProcessedLineItems.objects.filter(customer_line_item=order_item).aggregate(
            total_allocated=Sum('allocated_quantity'))['total_allocated'] or 0
        if allocated != order_item.request_quantity:
            all_fulfilled = False
            break

    # Update the order_processed status based on whether all items are fulfilled
    processed_order = instance.process_id
    processed_order.order_processed = all_fulfilled
    processed_order.save()

@receiver(post_save, sender=ProcessedLineItems)
def update_inventory_quantity(sender, instance, created, **kwargs):
    """
    Updates the available_quantity in the Inventory table when a ProcessedLineItems
    instance is created or updated.
    """
    # Determine the inventory item associated with the processed line item
    inventory_item = instance.inventory

    if created:
        # If the ProcessedLineItems instance is newly created,
        # decrease the available_quantity by the allocated_quantity
        inventory_item.available_quantity -= instance.allocated_quantity
    else:
        # If the instance is updated, adjust the available_quantity
        # by the difference between the new and old allocated quantities
        original_allocated_quantity = instance.__class__.objects.get(pk=instance.pk).allocated_quantity
        difference = instance.allocated_quantity - original_allocated_quantity
        inventory_item.available_quantity -= difference

    # Save the updated inventory item
    inventory_item.save()
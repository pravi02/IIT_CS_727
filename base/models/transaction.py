from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from base.models.customer import Customer, CustomerOrderItems, CustomerOrder
from base.models.inventory import Inventory
from django.utils import timezone

class ProcessedOrder(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    sales_amount = models.FloatField(default=0)
    processed_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    customer_order = models.OneToOneField(CustomerOrder, on_delete=models.CASCADE)
    order_processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'order_process'

    def __str__(self):
        return f"Processed Order {self.transaction_id} - {self.order_processed}"

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True).all()

    @classmethod
    def get_specific(cls, transaction_id):
        return cls.objects.filter(transaction_id=transaction_id).first()

class ProcessedLineItems(models.Model):
    line_item_id = models.AutoField(primary_key=True)
    customer_line_item= models.ForeignKey(CustomerOrderItems, on_delete=models.RESTRICT, related_name='processed_items')
    process_id = models.ForeignKey(ProcessedOrder, on_delete=models.CASCADE, related_name='transaction_items')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    allocated_quantity = models.IntegerField()



    class Meta:
        db_table = 'processed_line_items'

    def __str__(self):
        return f"ProcessedLineItem {self.line_item_id} - {self.allocated_quantity} units"

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True).all()

    @classmethod
    def get_specific(cls, line_item_id):
        return cls.objects.filter(line_item_id=line_item_id).first()





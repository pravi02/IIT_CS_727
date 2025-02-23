from django.contrib.auth.models import User
from django.db import models

from base.models.customer import Customer, CustomerOrderItems
from base.models.inventory import Inventory


class OrderProcess(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateField()
    sales_amount = models.FloatField()
    processed_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    customer_order = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order_processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'order_process'

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True).all()

    @classmethod
    def get_specific(cls, transaction_id):
        return cls.objects.filter(transaction_id=transaction_id).first()

class ProcessedLineItems(models.Model):
    line_item_id = models.AutoField(primary_key=True)
    customer_line_item= models.ForeignKey(CustomerOrderItems, on_delete=models.RESTRICT, related_name='processed_items')
    process_id = models.ForeignKey(OrderProcess, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    allocated_quantity = models.IntegerField()

    class Meta:
        db_table = 'processed_line_items'

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True).all()

    @classmethod
    def get_specific(cls, line_item_id):
        return cls.objects.filter(line_item_id=line_item_id).first()





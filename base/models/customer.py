from datetime import timezone, datetime

from django.db import models

from base.models.product import Product


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_location = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_telephone = models.CharField(max_length=20)

    class Meta:
        db_table = 'customer'
        unique_together = ('customer_name', 'customer_location', 'customer_telephone')

    def __str__(self):
        return self.customer_name



class CustomerOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'customer_order'


class CustomerOrderItems(models.Model):
    line_item_id = models.AutoField(primary_key=True)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='order_line_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    request_quantity = models.IntegerField()

    class Meta:
        db_table = 'customer_order_items'


    # @classmethod
    # def total_qty(cls):
    #     return cls.objects.aggregate(models.Sum('request_quantity'))['request_quantity__sum']


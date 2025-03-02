
from django.db import models

from base.models.product import Product

class InventoryLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    aisle_number = models.CharField(max_length=50)
    bin_location = models.CharField(max_length=50)

    class Meta:
        db_table = 'inventory_location'
        unique_together = ["aisle_number", "bin_location"]

    def __str__(self):
        return self.bin_location

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    available_quantity = models.IntegerField()
    reorder_trigger_quantity  = models.IntegerField(default=10)
    inventory_status = models.BooleanField(default=True)
    inventory_location = models.ForeignKey(InventoryLocation, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'inventory'
        unique_together = ["product", "inventory_location"]

    def __str__(self):
        return f"{self.product.product_name} - Location: {self.inventory_location.bin_location} - Qty Available: {self.available_quantity}"

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=True).all()

    @classmethod
    def get_specific(cls, inventory_id):
        return cls.objects.filter(inventory_id=inventory_id).first()


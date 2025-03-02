# Create your models here.
from django.db import models


class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_category'
        unique_together = ["category_name"]

    def __str__(self):
        return self.category_name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_contact_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'supplier'
        unique_together = ["supplier_name", "supplier_contact_number"]

    def __str__(self):
        # return f"{0 if self.supplier_id<=9 else ''}{self.supplier_id}  -  {self.supplier_name}"
        return self.supplier_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    serial_no = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_weight = models.FloatField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    product_supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'product'
        unique_together = ["product_name", "product_category"]

    def __str__(self):
        return f"{self.product_name}"





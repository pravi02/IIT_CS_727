from django import forms

from base.forms.custom_fields import UpperCaseCharField
from base.models.inventory import Inventory, InventoryLocation


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory

        exclude = [id,]

class InventoryLocationForm(forms.ModelForm):
    class Meta:
        model = InventoryLocation
        aisle_number = UpperCaseCharField()
        exclude = [id,]
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import TemplateView


from base.forms.inventory import InventoryForm, InventoryLocationForm
from base.models.inventory import Inventory, InventoryLocation
from base.views.common_view import CustomDeleteView


class InventoryView(TemplateView):
    # paginate_by = 20
    # model = Inventory
    template_name = "inventory.html"

    def post(self, request, *args, **kwargs):
        form = None
        if 'form1' in self.request.POST:
            form = InventoryForm(self.request.POST)
        elif 'form2' in self.request.POST:
            form = InventoryLocationForm(self.request.POST)
        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'Data saved at id: {data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return super(InventoryView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inventory'] = Inventory.objects.all().order_by('pk')
        context['location'] = InventoryLocation.objects.all().order_by('pk')
        context['form1'] = InventoryForm()
        context['form2'] = InventoryLocationForm()
        return context



class InventoryDelete(CustomDeleteView):
    model = Inventory
    messages_name = "Inventory"
    success_url = reverse_lazy('inventory-home')

class InventoryLocationDelete(CustomDeleteView):
    model = InventoryLocation
    messages_name = "Inventory Location"
    success_url = reverse_lazy('inventory-home')





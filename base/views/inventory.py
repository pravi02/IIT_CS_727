from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect

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
        form = InventoryForm(self.request.POST)
        inventory_id = request.POST.get('inventory_id')
        if inventory_id:
            inventory = get_object_or_404(Inventory, pk=inventory_id)
            form = InventoryForm(self.request.POST, instance=inventory)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'Data saved at id: {data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('inventory-home')
        # return super(InventoryView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inventory = Inventory.objects.all().order_by('pk')
        paginator_inventory = Paginator(inventory, 10)
        inventory_page_number = self.request.GET.get('inventory_page')
        context['inventory'] = paginator_inventory.get_page(inventory_page_number)
        context['form'] = InventoryForm()

        return context



class InventoryDelete(CustomDeleteView):
    model = Inventory
    messages_name = "Inventory"
    success_url = reverse_lazy('inventory-home')






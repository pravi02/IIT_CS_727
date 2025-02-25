from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import TemplateView


from base.forms.inventory import InventoryForm, InventoryLocationForm
from base.models.inventory import Inventory, InventoryLocation
from base.views.common_view import CustomDeleteView


class InventoryLocationView(TemplateView):
    # paginate_by = 20
    # model = Inventory
    template_name = "inventory_location.html"

    def post(self, request, *args, **kwargs):
        form = InventoryLocationForm(self.request.POST)
        location_id = request.POST.get('location_id')
        if location_id:
            location = get_object_or_404(InventoryLocation, pk=location_id)
            form = InventoryLocationForm(self.request.POST, instance=location)

        if form is not None and form.is_valid():
            data = form.save()
            messages.success(request, f'Data saved at id: {data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('inventory-location-home')
        # return super(InventoryView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inventory_location = InventoryLocation.objects.all().order_by('pk')
        paginator_inventory_location = Paginator(inventory_location, 10)
        location_page_number = self.request.GET.get('location_page')
        context['location'] = paginator_inventory_location.get_page(location_page_number)
        context['form'] = InventoryLocationForm()
        return context



class InventoryLocationDelete(CustomDeleteView):
    model = InventoryLocation
    messages_name = "Inventory Location"
    success_url = reverse_lazy('inventory-location-home')





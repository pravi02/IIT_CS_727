from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from base.forms.customer import CustomerForm
from base.models.customer import Customer
from base.views.common_view import CustomDeleteView


class CustomerListView(ListView):
    paginate_by = 20
    model = Customer
    template_name = "customer.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "POST":
            form = CustomerForm(self.request.POST)
            if form.is_valid():
                form.save()
        elif self.request.method == "GET":
            pass
        # form = CustomerForm(self.request.GET)
        # if form.is_valid():
        #     query = form.cleaned_data['query']
        #     queryset = queryset.filter(name__icontains=query)
        return queryset

    def post(self, request, *args, **kwargs):
        return super(CustomerListView, self).get(request, *args, **kwargs) #self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = CustomerForm()
        return context

class CustomerDelete(CustomDeleteView):
    model = Customer
    messages_name = "Customer"
    success_url = reverse_lazy("customer-home")


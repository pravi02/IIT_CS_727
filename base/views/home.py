from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from base.models.customer import CustomerOrder, Customer
from base.models.inventory import Inventory
from base.models.product import Product


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['inventory'] = Inventory.objects.all().count()
        context['product'] = Product.objects.all().count()
        context['orders'] = CustomerOrder.objects.all().count()
        context['customer'] = Customer.objects.all().count()
        return context


def index(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, world. You're at the index.")

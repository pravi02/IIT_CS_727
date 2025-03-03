from django.db.models import Count, F, Func, Value, CharField, ExpressionWrapper, DecimalField, Sum, Window
from django.db.models.functions import Substr, Length, Round, TruncDate
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from base.models.customer import CustomerOrder, Customer, CustomerOrderItems
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
        context['orders_by_country'] = get_orders_by_country()
        context['average_order_value_by_country'] = get_average_order_value_by_country()
        context['total_sales_by_category'] = get_total_sales_by_category()
        return context


def index(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, world. You're at the index.")


def get_orders_by_country():
    # the customer_location is of the form 'City, Country'
    # We use Substr to extract the country from the customer_location field (splitting by the comma)
    # we are getting count of customer order by Country

    country_orders = (CustomerOrder.objects
                      .values(
                          country=Func(
                              F('customer__customer_location'),
                              Value(',', output_field=CharField()),  # Delimiter (comma)
                              Value(-1),  # The '-1' extracts the part after the last comma
                              function='SUBSTRING_INDEX',
                              output_field=CharField()  # Explicitly set the output field to CharField
                          )
                      )
                      .annotate(order_count=Count('order_id'))  # Count the number of orders
                      .order_by('country'))  # Order by country

    return country_orders



def get_average_order_value_by_country():
    # Aggregate orders by country and calculate total order value and average order value
    country_orders = (
        CustomerOrder.objects
        .values(
            country=Func(
                F('customer__customer_location'),
                Value(',', output_field=CharField()),  # Delimiter (comma)
                Value(-1),  # Extract part after the last comma (i.e., the country)
                function='SUBSTRING_INDEX',
                output_field=CharField()
            )
        )
        .annotate(
            # Calculate total order value for each country by summing all line items' value
            total_order_value=Sum(
                F('order_line_items__product__price_per_unit') * F('order_line_items__request_quantity')
            ),
            # Count the number of distinct orders for each country
            order_count=Count('order_id', distinct=True)  # Count distinct orders based on order_id
        )
        .annotate(
            # Calculate the average order value and round to 2 decimal places
            average_order_value=Round(
                ExpressionWrapper(
                    F('total_order_value') / F('order_count'),  # Average is total value divided by order count
                    output_field=DecimalField(max_digits=10, decimal_places=2)
                ),
                2  # Round to 2 decimal places
            )
        )
        .order_by('country')  # Order the results by country
    )

    return country_orders




def get_total_sales_by_category():
    # Aggregate the total sales value by product category
    total_sales_by_category = (
        CustomerOrderItems.objects
        .select_related('product')  # Ensure product details are fetched
        .values('product__product_category__category_name')  # Group by product category name
        .annotate(
            total_sales_value=Sum(
                F('product__price_per_unit') * F('request_quantity')
            )  # Total sales value for each category
        )
        .order_by('product__product_category__category_name')  # Optionally, order by category name
    )

    return total_sales_by_category







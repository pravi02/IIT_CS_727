from django.conf.urls.static import static
from django.urls import path

from Inventory import settings
from base.views import home
from base.views.customer import CustomerListView, CustomerDelete
from base.views.customer_order import CustomerOrderListView, CustomerOrderDelete
from base.views.home import HomeView
from base.views.inventory import InventoryView, InventoryDelete, InventoryLocationDelete
from base.views.product import ProductListView, SupplierDelete, ProductDelete, ProductCategoryDelete

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('customer', CustomerListView.as_view(), name='customer-home'),
    path('orders', CustomerOrderListView.as_view(), name='orders-home'),
    path('products', ProductListView.as_view(), name='product-home'),
    path('inventory', InventoryView.as_view(), name='inventory-home'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
    path('customer_order/<int:pk>/delete', CustomerOrderDelete.as_view(), name='customer-order-delete'),
    path('inventory/<int:pk>/delete', InventoryDelete.as_view(), name='inventory-delete'),
    path('inventory_location/<int:pk>/delete', InventoryLocationDelete.as_view(), name='inventory-location-delete'),
    path('supplier/<int:pk>/delete', SupplierDelete.as_view(), name='supplier-delete'),
    path('product/<int:pk>/delete', ProductDelete.as_view(), name='product-delete'),
    path('product_category/<int:pk>/delete', ProductCategoryDelete.as_view(), name='product-category-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
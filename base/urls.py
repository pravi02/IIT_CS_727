from django.conf.urls.static import static
from django.urls import path

from Inventory import settings
from base.views import home
from base.views.customer import CustomerListView, CustomerDelete
from base.views.customer_order import CustomerOrderListView, CustomerOrderDelete, CustomerOrderItemDelete
from base.views.customer_order_processed import CustomerOrderProcessedListView
from base.views.home import HomeView
from base.views.inventory import InventoryView, InventoryDelete
from base.views.inventory_location import InventoryLocationView, InventoryLocationDelete
from base.views.login import CustomLoginView
from base.views.product import ProductListView, ProductDelete
from base.views.product_category import ProductCategoryListView, ProductCategoryDelete
from base.views.supplier import ProductSupplierListView, ProductSupplierDelete
from base.views.user import UserListView, UserDelete

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name="home"),
    path('customer', CustomerListView.as_view(), name='customer-home'),
    path('user', UserListView.as_view(), name='user-home'),
    path('orders', CustomerOrderListView.as_view(), name='orders-home'),
    path('processed', CustomerOrderProcessedListView.as_view(), name='processed-home'),
    path('products', ProductListView.as_view(), name='product-home'),
    path('category', ProductCategoryListView.as_view(), name='product-category-home'),
    path('supplier', ProductSupplierListView.as_view(), name='product-supplier-home'),
    path('inventory', InventoryView.as_view(), name='inventory-home'),
    path('location', InventoryLocationView.as_view(), name='inventory-location-home'),
    path('inventory_location/<int:pk>/delete', InventoryLocationDelete.as_view(), name='inventory-location-delete'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
    path('customer_order/<int:pk>/delete', CustomerOrderDelete.as_view(), name='customer-order-delete'),
    path('customer_order_item/<int:pk>/delete', CustomerOrderItemDelete.as_view(), name='customer-order-item-delete'),
    path('inventory/<int:pk>/delete', InventoryDelete.as_view(), name='inventory-delete'),
    path('user/<int:pk>/delete', UserDelete.as_view(), name='user-delete'),

    path('supplier/<int:pk>/delete', ProductSupplierDelete.as_view(), name='product-supplier-delete'),
    path('product/<int:pk>/delete', ProductDelete.as_view(), name='product-delete'),
    path('product_category/<int:pk>/delete', ProductCategoryDelete.as_view(), name='product-category-delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
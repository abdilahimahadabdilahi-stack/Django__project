from django.urls import path
from . import views

urlpatterns = [
    # Auth URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Product URLs
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/add/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.customer_create, name='customer_create'),
    path('customer/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # Store URLs
    path('stores/', views.store_list, name='store_list'),
    path('store/add/', views.store_create, name='store_create'),
    path('store/<int:pk>/edit/', views.store_update, name='store_update'),
    path('store/<int:pk>/delete/', views.store_delete, name='store_delete'),

    # Supplier URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('supplier/add/', views.supplier_create, name='supplier_create'),
    path('supplier/<int:pk>/edit/', views.supplier_update, name='supplier_update'),
    path('supplier/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),

    # Payment URLs
    path('payments/', views.payment_list, name='payment_list'),
    path('payment/add/', views.payment_create, name='payment_create'),

    # Report URLs
    path('reports/', views.report_list, name='report_list'),
    path('report/add/', views.report_create, name='report_create'),
    path('register/', views.register_view, name='register'),
]
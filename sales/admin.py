from django.contrib import admin
from .models import Customer, Product, Supplier, Store, Payment, Report


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Store)
admin.site.register(Payment)
admin.site.register(Report)

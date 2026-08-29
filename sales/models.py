from django.db import models
from django.contrib.auth.models import User

# Store / Dukaanka ama Bakhaarka
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # Ku xir Django User si uu Login/Sign in u samaysan karo
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    sales_person = models.CharField(max_length=100)
    address = models.TextField()
    # Waxaa fiican in Supplier-ka uu si toos ah ula xiriiro Product
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.sales_person

# Payment / Lacag Bixinta
class Payment(models.Model):
    PAYMENT_METHODS = (
        ('EVC', 'EVC Plus'),
        ('ZAAD', 'ZAAD Service'),
        ('SAHAL', 'Sahal'),
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - ${self.amount}"

# Report / Warbixinaha Sabuurada
class Report(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%Y-%m-%d')}"
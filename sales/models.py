from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    sales_person = models.CharField(max_length=100)
    address = models.TextField()
    product = models.CharField(max_length=100)  # No relationship
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.sales_person
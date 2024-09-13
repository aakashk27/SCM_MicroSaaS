from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Factory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='factories')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    max_capacity = models.PositiveIntegerField()
    production_rate = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Production rate per unit of time")

    def __str__(self):
        return self.name
    

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit in Rupees")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
    
class DistributionCenter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='distribution_centers')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    max_storage_capacity = models.PositiveIntegerField()
    current_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    demand_forecast = models.PositiveIntegerField(help_text="Demand forecast per unit of time")

    def __str__(self):
        return self.name


class Transportation(models.Model):
    mode = models.CharField(max_length=50)
    max_load_capacity = models.PositiveIntegerField()
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mode} - Capacity: {self.capacity}"
    

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE, related_name='inventories')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.distribution_center.name} - Stock: {self.stock}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.customer.name} - Quantity: {self.quantity}"




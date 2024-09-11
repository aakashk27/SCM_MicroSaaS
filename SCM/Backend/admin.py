from django.contrib import admin
from Backend.models import Factory, Product, DistributionCenter, Customer, Transportation, Inventory

@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'max_capacity', 'production_rate']
    search_fields = ['name', 'location']
    list_filter = ['location',]
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'factory']
    search_fields = ['name', 'factory__name']
    list_filter = ['factory',]
    list_per_page = 10


@admin.register(DistributionCenter)
class DistributionCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'max_storage_capacity', 'current_stock']
    search_fields = ['name', 'location']
    list_filter = ['location',]
    list_per_page = 10


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'demand_forecast']
    search_fields = ['name', 'location']
    list_filter = ['location',]
    list_per_page = 10


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ['mode', 'max_load_capacity', 'cost_per_km']
    search_fields = ['mode',]
    list_filter = ['mode',]
    list_per_page = 10


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'stock', 'distribution_center']
    search_fields = ['product__name',]
    list_filter = ['product', 'distribution_center']
    list_per_page = 10




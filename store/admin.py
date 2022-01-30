from . import models
from django.contrib import admin

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from . models import Categories, Customer, Product, Order


# Register your models here.
admin.site.register(Categories)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
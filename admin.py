from django.contrib import admin

# Register your models here.
from . models import Product
from . models import Order
from . models import Customer
from . models import Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
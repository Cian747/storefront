from django.contrib import admin
from .models import Customer,Category,Products,Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)

from django.contrib import admin

# Register your models here.
from .models import *

# Register to see on the Admin panel
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

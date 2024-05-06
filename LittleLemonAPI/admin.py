from django.contrib import admin
from .models import Cart, MenuItem, Category, Order, OrderItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
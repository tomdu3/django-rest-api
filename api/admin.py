from django.contrib import admin
from .models import User, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    """
    Inline admin for OrderItem - it shows the related product name and quantity
    """
    model = OrderItem
    
class OrderAdmin(admin.ModelAdmin):
    """
    Admin for Order - it shows the order id, user, status and created at
    """
    list_display = ('order_id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username')
    inlines = (OrderItemInline,)
    
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
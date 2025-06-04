from rest_framework import serializers
from api.models import (
    Product,
    Order,
    OrderItem,
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'description',
            'stock',
            'image'
        )

    def validate_stock(self, value: int):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be less than 0')
        return value

    def validate_price(self, value: float):
        if value <= 0:
            raise serializers.ValidationError('Price has to be greater than 0')
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    # takes the name from the product model
    product_name = serializers.CharField(
        source='product.name'
        )
    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2
        )
    # if wish to show all product model details, then remove product_name and
    # product_price from fields
    # product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            'product',
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        )



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True,
        read_only=True
        )
    # takes method get_total_price (by default)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self, obj):
       order_items = obj.items.all()
       return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'status',
            'created_at',
            'items',
            'total_price'
            )



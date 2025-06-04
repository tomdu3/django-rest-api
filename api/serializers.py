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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'status',
            'created_at',
            'updated_at'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'order',
            'product',
            'quantity'
        )


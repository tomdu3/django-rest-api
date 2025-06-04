from api.serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer
)
from api.models import (
    Product,
    Order,
    OrderItem,
)


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

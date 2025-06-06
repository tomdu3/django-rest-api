from django.db.models import Max
from api.serializers import (
    ProductSerializer,
    OrderSerializer,
    ProductInfoSerializer
)
from api.models import (
    Product,
    Order,
    OrderItem,
)


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics


class ProductListAPIView(generics.ListAPIView):
    # filter products that are in stock
    queryset = Product.objects.filter(stock__gt=0)
    
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'  # items__product is the related name in OrderItem
        ).all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def order_detail(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer(
        {
        'products': products,
        'count': products.count(),
        'max_price': products.aggregate(
            max_price=Max('price'))['max_price']
        }
    )
    return Response(serializer.data)
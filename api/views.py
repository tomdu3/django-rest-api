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
    # prefetch_related to avoid N+1 query problem
    # it optimizes the query by fetching related objects in a single query
    orders = Order.objects.prefetch_related(
        'items', 'items__product'  # items__product is the related name in OrderItem
        ).all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

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
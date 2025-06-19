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
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProductListAPIView(generics.ListAPIView):
    # filter products that are in stock
    # queryset = Product.objects.filter(stock__gt=0)
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        # items__product is the related name in OrderItem
        'items', 'items__product'
        ).all()
    serializer_class = OrderSerializer
    

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
        ).all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': products.count(),
            'max_price': products.aggregate(
                max_price=Max('price'))['max_price']
            })
        return Response(serializer.data)


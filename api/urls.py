from django.urls import path
from . import views

urlpatterns = [
    path(
        'products/',
        views.ProductListCreateAPIView.as_view(),
        name='product_list'
        ),
    path(
        'products/<int:product_id>/',
        views.ProductDetailAPIView.as_view(),
        name='product_detail'
        ),
    path(
        'products/info/',
        views.ProductInfoAPIView.as_view(),
        name='product_info'),
    path('orders/', views.OrderListAPIView.as_view(), name='order_list'),
    path(
        'orders/user/',
        views.UserOrderListAPIView.as_view(),
        name='user_order_list'
        ),
]

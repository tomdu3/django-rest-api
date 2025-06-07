from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path(
        'products/<int:pk>/',
        views.ProductDetailAPIView.as_view(),
        name='product_detail'
        ),
    path('products/info/', views.product_info, name='product_info'),
    path('orders/', views.OrderListAPIView.as_view(), name='order_list'),
    path('orders/<uuid:order_id>/', views.order_detail, name='order_detail'),
    path(
        'orders/user/',
        views.UserOrderListAPIView.as_view(),
        name='user_order_list'
        ),
]

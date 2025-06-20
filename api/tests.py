from django.test import TestCase
from api.models import User, Order
from rest_framework.reverse import reverse
from rest_framework import status

class UserOrderListAPITestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username='user1',
            password='password1',
            email='user1@example.com'
        )
        user2 = User.objects.create_user(
            username='user2',
            password='password2',
            email='user2@example.com'
        )
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)
        
    def test_user_order_retrieves_only_authenticated_user_orders(self):
        # login as user1
        user = User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user_order_list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        orders = response.json()
        print(orders)
        self.assertTrue(all(order['user'] == user.id for order in orders))
    
    def test_user_order_list_unauthenticated_user(self):
        response = self.client.get(reverse('user_order_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import lorem_ipsum
from api.models import User, Product, Order, OrderItem


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(
                username='admin', password='test', email='admin@admin.com')

        # create products - name, desc, price, stock, image
        products = [
            Product(name="Radio Transistor", description=lorem_ipsum.paragraph(
            ), price=Decimal('12.99'), stock=4),
            Product(name="Mini Fridge", description=lorem_ipsum.paragraph(),
                    price=Decimal('70.99'), stock=6),
            Product(name="Portable Hi-Fi", description=lorem_ipsum.paragraph(),
                    price=Decimal('15.99'), stock=11),
            Product(name="Soundspeaker", description=lorem_ipsum.paragraph(
            ), price=Decimal('17.99'), stock=2),
            Product(name="Microphone", description=lorem_ipsum.paragraph(),
                    price=Decimal('35.99'), stock=4),
            Product(name="Guitar", description=lorem_ipsum.paragraph(),
                    price=Decimal('500.05'), stock=0),
        ]

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()

        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1, 3)
                )

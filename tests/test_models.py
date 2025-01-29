from django.test import TestCase
from dropship_project.models import CustomUser, Product, CartItem, Order

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password'))

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Product 1')
        self.assertEqual(self.product.description, 'Description 1')
        self.assertEqual(self.product.cost_price, 10)
        self.assertEqual(self.product.selling_price, 15)

    def test_product_clean(self):
        with self.assertRaises(Exception):
            Product.objects.create(name='Product 2', description='Description 2', cost_price=20, selling_price=15)

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.user, self.user)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 1)

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        self.order = Order.objects.create(user=self.user, total_price=15)
        self.order.items.set([self.cart_item])

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total_price, 15)
        self.assertEqual(self.order.items.count(), 1)
        self.assertEqual(self.order.items.first(), self.cart_item)

    def test_order_process(self):
        success = self.order.process_order()
        self.assertTrue(success)
        self.assertEqual(self.order.status, 'processing')

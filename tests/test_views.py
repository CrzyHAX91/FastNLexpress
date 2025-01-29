from django.test import TestCase, Client
from django.urls import reverse
from dropship_project.models import Product, CustomUser, CartItem, Order

class ProductListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('product_list')
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', cost_price=20, selling_price=25)

    def test_product_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.url = reverse('product_detail', args=[self.product.id])

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)

class AddToCartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.url = reverse('add_to_cart', args=[self.product.id])

    def test_add_to_cart_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CartItem.objects.filter(user=self.user, product=self.product).exists())

class CartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        self.url = reverse('cart')

    def test_cart_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.cart_item.quantity)

class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        self.url = reverse('checkout')

    def test_checkout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.cart_item.quantity)

class OrderConfirmationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(name='Product 1', description='Description 1', cost_price=10, selling_price=15)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        self.order = Order.objects.create(user=self.user, total_price=15)
        self.order.items.set([self.cart_item])
        self.url = reverse('order_confirmation', args=[self.order.id])

    def test_order_confirmation_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_confirmation.html')
        self.assertContains(response, self.order.id)
        self.assertContains(response, self.product.name)

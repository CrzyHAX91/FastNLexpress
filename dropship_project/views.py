from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.db.models import F, Sum
from .models import Product, CartItem, Order
from integrations.aliexpress_integration import sync_products
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View

def is_admin(user):
    """Check if the user is an admin."""
    return user.is_staff or user.is_superuser

class AdminRequiredMixin(UserPassesTestMixin):
    """Mixin to ensure the user is an admin."""
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class ProductListView(View):
    """View for listing all products."""
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})

class ProductDetailView(View):
    """View for displaying the details of a specific product."""
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    """Add a product to the shopping cart."""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity = F('quantity') + 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    """View for displaying the shopping cart."""
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    total = cart_items.aggregate(total=Sum(F('product__selling_price') * F('quantity')))['total'] or 0
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    """View for the checkout process."""
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    total = cart_items.aggregate(total=Sum(F('product__selling_price') * F('quantity')))['total'] or 0
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total)
        order.items.set(cart_items)
        cart_items.delete()
        success = order.process_order()
        if success:
            return redirect('order_confirmation', order_id=order.id)
        else:
            return render(request, 'order_failed.html', {'order': order})
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def order_confirmation(request, order_id):
    """View for order confirmation."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})

class AdminDashboardView(AdminRequiredMixin, View):
    """View for the admin dashboard."""
    def get(self, request):
        recent_orders = Order.objects.all().order_by('-created_at')[:10]
        total_sales = Order.objects.aggregate(total=Sum('total_price'))['total'] or 0
        return render(request, 'admin_dashboard.html', {
            'recent_orders': recent_orders,
            'total_sales': total_sales
        })

class SyncAliexpressProductsView(AdminRequiredMixin, View):
    """View for syncing products from AliExpress."""
    def post(self, request):
        sync_products()
        return JsonResponse({'status': 'success', 'message': 'Products synced successfully'})

class HelpdeskView(View):
    """View for the AI helpdesk."""
    def get(self, request):
        return render(request, 'helpdesk.html')

    def post(self, request):
        user_query = request.POST.get('query', '')
        response = generate_response(user_query)  # Placeholder for AI response generation
        return JsonResponse({'response': response})

def generate_response(query):
    """Generate a placeholder response for the AI helpdesk."""
    return "This is a placeholder response for your query: " + query

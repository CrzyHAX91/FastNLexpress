
import os
from aliexpress_api import AliexpressApi, AliexpressCategory
from .models import Product

# Replace these with your actual AliExpress API credentials
APP_KEY = os.environ.get('ALIEXPRESS_APP_KEY')
APP_SECRET = os.environ.get('ALIEXPRESS_APP_SECRET')

api = AliexpressApi(APP_KEY, APP_SECRET)

def sync_products():
    # Fetch products from AliExpress API
    products = api.get_product_list(
        fields="productId,productTitle,productUrl,imageUrl,salePrice",
        keywords="dropshipping",
        page_size=20
    )

    for product in products:
        # Check if the product already exists in our database
        existing_product = Product.objects.filter(aliexpress_url=product['productUrl']).first()

        if existing_product:
            # Update existing product
            existing_product.name = product['productTitle']
            existing_product.selling_price = float(product['salePrice']['amount'])
            existing_product.save()
        else:
            # Create new product
            new_product = Product(
                name=product['productTitle'],
                description=f"AliExpress Product ID: {product['productId']}",
                cost_price=float(product['salePrice']['amount']),
                selling_price=float(product['salePrice']['amount']) * 1.5,  # 50% markup
                aliexpress_url=product['productUrl']
            )
            new_product.save()

def place_order(order):
    # This is a simplified example. In a real-world scenario, you'd need to handle
    # shipping addresses, payment confirmation, etc.
    for item in order.items.all():
        product = item.product
        quantity = item.quantity

        # Place order on AliExpress
        aliexpress_order = api.create_order(
            product_id=product.aliexpress_url.split('/')[-1],  # Assuming the product ID is the last part of the URL
            quantity=quantity,
            shipping_address={
                # Add shipping address details here
            }
        )

        if aliexpress_order:
            order.status = 'processing'
            order.save()
            return True
    return False

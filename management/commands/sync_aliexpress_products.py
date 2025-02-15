from django.core.management.base import BaseCommand
from dropship_project.aliexpress_integration import sync_products

class Command(BaseCommand):
    help = 'Sync products from AliExpress'

    def handle(self, *args, **kwargs):
        sync_products()
        self.stdout.write(self.style.SUCCESS('Successfully synced products from AliExpress'))

from django.core.management.base import BaseCommand
from dropship_project.models import Product

class Command(BaseCommand):
    help = 'Populate the database with initial product data'

    def handle(self, *args, **kwargs):
        # Add your product population logic here
        self.stdout.write(self.style.SUCCESS('Successfully populated products'))

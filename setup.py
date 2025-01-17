import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dropship_project.settings")
django.setup()

def setup_project():
    """Set up the project environment."""
    call_command('migrate')
    call_command('collectstatic', interactive=False)

if __name__ == "__main__":
    setup_project()

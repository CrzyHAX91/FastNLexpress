import time
import subprocess
import os
import sys
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_sync_command():
    manage_py_path = os.path.join(os.path.dirname(__file__), 'dropship_project', 'manage.py')
    try:
        subprocess.run([sys.executable, manage_py_path, 'sync_aliexpress_products'], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running sync command: {e}")

def main():
    while True:
        now = datetime.now()
        next_run = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        time_to_wait = (next_run - now).total_seconds()
        
        logging.info(f"Next sync scheduled at {next_run}")
        time.sleep(time_to_wait)
        
        logging.info("Running AliExpress product sync...")
        run_sync_command()

if __name__ == "__main__":
    main()


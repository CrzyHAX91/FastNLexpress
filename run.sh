#!/bin/bash

# Navigate to the project directory
cd "C:/Users/Behee/Desktop/Dropship dbug/dropshipv2"

# Activate virtual environment (if you're using one)
# source /path/to/your/virtualenv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run setup script
python setup.py

# Set Cloudflare environment variables
export CLOUDFLARE_API_KEY=your_cloudflare_api_key
export CLOUDFLARE_EMAIL=your_email@example.com

# Run the development server
python dropship_project/manage.py runserver 0.0.0.0:8000

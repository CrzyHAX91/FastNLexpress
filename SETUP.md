# Setting Up the Development Environment for Dropship V2

This guide will walk you through the process of setting up a development environment for the Dropship V2 project.

## Prerequisites

- Python 3.9 or higher
- Django 3.2 or higher
- Virtual environment (recommended)

## Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/CrzyHAX91/dropshipv2.git
   cd dropshipv2
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv new_venv
   ```

3. **Activate the virtual environment**:
   - On Windows:

     ```bash
     new_venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source new_venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

## Additional Information

For more details, refer to the documentation in the repository.

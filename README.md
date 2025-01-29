# Dropship V2

Dropship V2 is an automated dropshipping application that integrates with AliExpress and includes an AI-assisted Helpdesk.

## Features

- Automatic product syncing with AliExpress
- User-friendly interface
- Comprehensive order management
- Email notifications for order updates

## Installation

Follow the instructions in the `SETUP.md` file to set up the development environment.

## Contributing

We welcome contributions! Please refer to the `CONTRIBUTING.md` file for guidelines. Ensure you are using `actions/checkout@v4` in your workflows.
## License

This project is licensed under the MIT License.

## Setup Instructions

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

## Usage Examples

### Syncing Products from AliExpress

To sync products from AliExpress, run the following management command:

```bash
python manage.py sync_aliexpress_products
```

### Adding Products

To add products to the database, use the following management command:

```bash
python manage.py populate_and_add_products
```

### Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## Contribution Guidelines

We welcome contributions! Please follow these steps to contribute:

1. **Fork the repository**: Create a personal copy of the repository on GitHub.
2. **Create a new branch**: Use a descriptive name for your branch.
3. **Make your changes**: Implement your changes in your branch.
4. **Submit a pull request**: Once your changes are ready, submit a pull request to the main repository.

## Code Organization and Structure

The repository is organized as follows:

- `integrations/`: Contains integration-related code, such as the `aliexpress_integration.py` file.
- `services/`: Contains business logic and service-related code, such as order processing and product synchronization.
- `dropship_project/`: Contains the main Django project files, including models, views, and templates.
- `tests/`: Contains unit tests for views, models, and utility functions.

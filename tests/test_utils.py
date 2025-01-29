from django.test import TestCase
from dropship_project.utils import calculate_profit_margin, suggest_selling_price

class UtilsTest(TestCase):
    def test_calculate_profit_margin(self):
        cost_price = 100
        selling_price = 150
        expected_margin = 50.0
        self.assertEqual(calculate_profit_margin(cost_price, selling_price), expected_margin)

    def test_suggest_selling_price(self):
        cost_price = 100
        target_margin = 20
        expected_selling_price = 120.0
        self.assertEqual(suggest_selling_price(cost_price, target_margin), expected_selling_price)

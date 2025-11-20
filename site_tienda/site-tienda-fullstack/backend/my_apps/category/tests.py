from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")
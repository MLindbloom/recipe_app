from django.test import TestCase
from .models import Recipe


# Create your tests here
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Brownies",
            cooking_time=45,
            ingredients="Brownie mix, Eggs, Oil, Water",
            description="Preheat oven to 350F. Add ingredients to a bowl and whisk together. Grease pan and pour mix into pan. Bake for approx. 45 minutes.",
        )

    # Get a Recipe Object to test
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    # Test Recipe Name Length
    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 120, "name has over 120 characters")

    # Test Cooking Time is an Integer
    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), int, "cooking_time is not a number")

    # Test Ingredients List Length
    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 240, "ingredients have over 240 characters")

    # Test Description Length
    def test_desciption_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("description").max_length
        self.assertEqual(max_length, 240, "description has over 240 characters")

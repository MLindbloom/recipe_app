from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=240)
    cooking_time = models.IntegerField(help_text="in minutes", default=0)
    description = models.TextField(max_length=240, default="No Description")

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"
        return difficulty

    def __str__(self):
        return str(self.name)

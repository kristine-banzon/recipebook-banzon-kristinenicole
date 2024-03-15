from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from datetime import datetime
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    creation = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_details', args=str(self.pk))
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=str(self.pk))
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='ingredients'
    )
    
    def __str__(self):
        return '{} {} in {}'.format(
            self.quantity, self.ingredient.name, self.recipe.name
        )
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(
        validators = [
            MinLengthValidator(255, "Your bio is too short. Input more data.")
        ]
    )
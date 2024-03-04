from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInLineAdmin(admin.TabularInline):
    model = RecipeIngredient
    

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    in_line = [RecipeIngredientInLineAdmin,]
    

admin.site.register(Recipe, RecipeAdmin)
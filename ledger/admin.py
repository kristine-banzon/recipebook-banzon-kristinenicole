from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Ingredient, Profile, Recipe, RecipeIngredient


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine]
    

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
        

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
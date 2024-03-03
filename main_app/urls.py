from django.urls import path
from .views import create_ingredient, create_recipe, edit_ingredient, edit_recipe, show_recipe

# /food/

urlpatterns = [
    path("create_recipe/", create_recipe, name="create-recipe"),
    path("create_ingredient/", create_ingredient, name="create-ingredient"),
    path("edit_ingredient/<id>", edit_ingredient, name="edit-ingredient"),
    path("edit_recipe/<id>", edit_recipe, name="edit-recipe"),
    path('<int:recipe_id>', show_recipe, name='show-recipe'),
]

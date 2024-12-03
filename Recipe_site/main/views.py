from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Recipe


def index(request):
    recipes = Recipe.objects.order_by('created_at')[:5]
    return render(request, 'home_page.html', context={'recipes': recipes})


class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'
    pk_url_kwarg = 'id'

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    # for ingredient in recipe.ingredients_recipe.all():
    #     print(ingredient)
    #     print(ingredient.unit)
    #     print(ingredient.quantity)
    return render(request, 'recipe.html', context={'recipe': recipe})
# Create your views here.

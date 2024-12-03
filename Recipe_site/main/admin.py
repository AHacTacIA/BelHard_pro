from django.contrib import admin
from django.contrib.auth.models import User

from main.models import Recipe, Review, Ingredient, Category, RecipeIngredient

# admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Ingredient)
admin.site.register(Category)


class RecipeIngredientInline(admin.TabularInline): # или admin.StackedInline для вертикального отображения
    model = RecipeIngredient
    extra = 1  # Количество пустых строк для добавления новых ингредиентов
    fields = ('ingredient', 'quantity', 'unit') # можно добавить 'unit' если поле есть в RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('title', 'author', 'instruction', 'cook_time')
    # ... другие настройки админки ...
#
# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     pass # Или другие настройки для Ingredient




# admin.site.register(User)
# Register your models here.

# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'categories', 'ingredients_quantity', 'instruction', 'cook_time')
#
#     def ingredients_quantity(self, obj):
#         ingredients = obj.ingredients
#         return f"{ingredients}"

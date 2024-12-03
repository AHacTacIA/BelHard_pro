from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# class User(models.Model):
#     username = models.CharField(max_length=20)
#     email = models.EmailField()
#     password = models.CharField()
#     bio = models.CharField(max_length=150, verbose_name='Описание')
#     avatar = models.ImageField(
#         default='',
#         upload_to=r'photos/%Y/%m/%d',
#         blank=True,
#         verbose_name="Фoто")
#
#     def __str__(self):
#         return f'{self.username}'
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         db_table = 'users'


# class Tag(models.Model):
#     tag = models.CharField()
#
#     def __str__(self):
#         return f'{self.tag}'

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categories'


class Ingredient(models.Model):
    # UNIT_CHOICES = [('кг', 'Килограмм'), ('гр', 'Грамм'), ('мг', 'Миллиграмм'), ('л', 'Литр'), ('мл', 'Миллилитр'),
    #                 ('стак.', 'Стакан'), ('стол.л.', 'Столовая ложка'), ('чайн.л.', 'Чайная ложка'),
    #                 ('десертн.л.', 'Десертная ложка'), ('шт.', 'Штука'), ]

    name = models.CharField(max_length=255)
    # unit = models.CharField(max_length=50, choices=UNIT_CHOICES, verbose_name='Ед.измерения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        db_table = 'ingredients'


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, related_name='recipes')  # through='RecipeCategory'
    title = models.CharField(max_length=100, verbose_name='Название')
    # ingredients = models.CharField(verbose_name='Ингредиенты')
    instruction = models.TextField(verbose_name='Инструкция')
    cook_time = models.IntegerField(verbose_name='Время готовки (мин)')
    servings = models.SmallIntegerField(verbose_name='Кол-во порций', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipes/%Y/%m/%d', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return f'Recipe - {self.title}, author - {self.author}'

    def get_absolute_url(self):
        return reverse('recipe', kwargs={"id": self.pk})

    def get_edit_url(self):
        return reverse('recipe_edit', kwargs={"id": self.pk})

    # image
    # video
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        db_table = 'recipes'


class RecipeIngredient(models.Model):
    UNIT_CHOICES = [('кг', 'Килограмм'), ('гр', 'Грамм'), ('мг', 'Миллиграмм'), ('л', 'Литр'), ('мл', 'Миллилитр'),
                    ('стак.', 'Стакан'), ('стол.л.', 'Столовая ложка'), ('чайн.л.', 'Чайная ложка'),
                    ('десертн.л.', 'Десертная ложка'), ('шт.', 'Штука'), ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE ,related_name='ingredients_recipe')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='Кол-во')
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, verbose_name='Ед.измерения')

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient.name} в {self.recipe.title}"

    class Meta:
        db_table = 'recipe_ingredient'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Оценка')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f'Recipe - {self.recipe}, commentator - {self.user}, rating - {self.rating}'

    def get_absolute_url(self):
        return reverse('review', kwargs={"id": self.pk})

    def get_edit_url(self):
        return reverse('review_edit', kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'reviews'

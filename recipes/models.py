from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)  # Название категории
    description = models.TextField(blank=True, null=True)  # Описание категории (необязательное поле)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Легкий'),
        ('medium', 'Средний'),
        ('hard', 'Сложный'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингредиенты", help_text="Каждый ингредиент с новой строки")
    cooking_steps = models.TextField(verbose_name="Шаги приготовления", help_text="Каждый шаг с новой строки")
    cooking_time = models.CharField(max_length=100, blank=True, null=True, verbose_name="Время готовки") # в минутах
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True, verbose_name="Фото")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ManyToManyField(
        Category, 
        through='RecipeCategory',
        related_name='recipes',
        verbose_name="Категории"
    )   # Связь с категорией
    
    # New fields
    difficulty = models.CharField(
        max_length=10, 
        choices=DIFFICULTY_CHOICES, 
        default='medium',
        verbose_name="Сложность"
    )
    servings = models.PositiveIntegerField(default=1, verbose_name="Порции")
    calories = models.PositiveIntegerField(default=0, verbose_name="Калории")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Категория рецепта"
        verbose_name_plural = "Категории рецептов"
        unique_together = ['recipe', 'category']


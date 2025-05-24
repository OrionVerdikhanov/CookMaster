from django import forms
from .models import Recipe, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image', 'category', 'difficulty', 
                 'servings', 'calories', 'ingredients', 'cooking_steps']
        labels = {
            'title': 'Название',
            'category': 'Категория',
            'cooking_steps': 'Шаги приготовления',
            'ingredients': 'Ингредиенты',
            'description': 'Описание',
            'image': 'Фото',
            'difficulty': 'Сложность',
            'servings': 'Количество порций',
            'calories': 'Калории',
        }

        widgets = {
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'Введите каждый ингредиент с новой строки\nНапример:\n2 яйца\n200г муки\n1 стакан молока'
            }),
            'cooking_steps': forms.Textarea(attrs={
                'placeholder': 'Введите каждый шаг с новой строки\nНапример:\n1. Смешать сухие ингредиенты\n2. Добавить яйца и молоко'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
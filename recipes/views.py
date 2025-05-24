from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category
from .forms import RecipeForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
import random
from django.contrib import messages
from django.db.models import Q, Count
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    categories = Category.objects.annotate(recipe_count=Count('recipes'))
    recipes = Recipe.objects.all()
    
    selected_category = request.GET.get('category')
    if selected_category:
        recipes = recipes.filter(category__name=selected_category)

    context = {
        'recipes': recipes,
        'categories': categories,
        'selected_category': selected_category
    }
    return render(request, 'recipes/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe,
        'home_url': reverse('recipes:home')  # Add the correct URL name
    }
    return render(request, 'recipes/recipe_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Ошибка регистрации'})
    else:
        form = UserRegistrationForm()
    return render(request, 'recipes/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('recipes:home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Неверное имя пользователя или пароль'})
    
    return render(request, 'recipes/login.html', {'form': AuthenticationForm()})

@login_required  # Доступ только для авторизованных пользователей
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Присваиваем автору текущего пользователя
            recipe.save()
            messages.success(request, 'Рецепт успешно создан!')
            return redirect('recipes:home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/recipe_form.html', {
        'form': form,
        'form_errors': form.errors
    })

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)  # Получаем рецепт по ID
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)  # Заполняем форму данными рецепта
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)  # Перенаправляем на страницу рецепта
    else:
        form = RecipeForm(instance=recipe)  # Если GET-запрос, просто отображаем форму

    return render(request, 'recipes/recipe_form.html', {'form': form, 'recipe': recipe})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()  # Удаляем рецепт
        messages.success(request, 'Рецепт удален успешно!')
        return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

@login_required
def profile(request):
    # Отображение профиля текущего пользователя
    user_recipes = Recipe.objects.filter(author=request.user)  # Рецепты текущего пользователя
    return render(request, 'recipes/profile.html', {'user_recipes': user_recipes})

def search_recipes(request):
    query = request.GET.get('q', '').strip()
    if query:
        # Using icontains for case-insensitive search and Q objects for OR conditions
        results = Recipe.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(cooking_steps__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    else:
        results = Recipe.objects.none()
    
    return render(request, 'recipes/search_results.html', {
        'query': query,
        'results': results
    })

def category_view(request, category):
    categories = Category.objects.annotate(recipe_count=Count('recipes'))
    recipes = Recipe.objects.filter(category__name=category)
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'recipes/index.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recipes:home')
    return redirect('recipes:home')
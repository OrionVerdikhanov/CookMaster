from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # Заменяем на новый login_view
    path('logout/', views.logout_view, name='logout'),  # Replace the existing logout path
    
    # Recipe CRUD operations
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    
    # Additional functionality
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_recipes, name='search'),
    path('category/<str:category>/', views.category_view, name='category'),
]
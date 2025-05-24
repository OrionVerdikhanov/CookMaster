from django.db import migrations

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('recipes', 'Category')
    categories = [
        'Завтраки',
        'Супы',
        'Салаты',
        'Закуски и тапас',
        'Основные блюда',
        'Мясные блюда',
        'Рыбные и морепродукты',
        'Блюда из птицы',
        'Паста, рис и крупы',
        'Вегетарианские рецепты',
        'Веганские рецепты',
        'Безглютеновые блюда',
        'Постные рецепты',
        'Выпечка и хлеб',
        'Десерты и сладости',
        'Напитки и коктейли',
        'Соусы, маринады и заправки',
        'Диетические и низкокалорийные блюда',
        'Быстрые и простые рецепты',
        'Праздничные и тематические меню',
    ]
    
    for category_name in categories:
        Category.objects.create(name=category_name)

def remove_default_categories(apps, schema_editor):
    Category = apps.get_model('recipes', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_categories, remove_default_categories),
    ]

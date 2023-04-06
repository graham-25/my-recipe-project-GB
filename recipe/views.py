from django.shortcuts import render
from .models import item

# Create your views here.
# Changed the function so that it makes sense.


def show_recipe_list(request):
    items = item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'recipe/recipe_list.html', context)

def add_item(request):
    return render(request, 'recipe/add_item.html')

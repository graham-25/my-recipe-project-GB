from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        item.objects.create(name=name, done=done)

        return redirect('recipe_list')
    return render(request, 'recipe/add_item.html')

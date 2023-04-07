from django.shortcuts import render, redirect
from .models import item
from .forms import ItemForm

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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'recipe/add_item.html', context)

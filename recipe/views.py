from django.shortcuts import render, redirect, get_object_or_404
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

def edit_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    form = ItemForm(instance=items)
    context = {
        'form': form
    }
    return render(request, 'recipe/edit_item.html', context)

def toggle_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    items.done = not items.done
    items.save()
    return redirect('get_recipe_list')

def delete_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    items.delete()
    return redirect('get_recipe_list')
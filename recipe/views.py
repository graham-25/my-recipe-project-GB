from django.shortcuts import render

# Create your views here.
# Changed the function so that it makes sense.
def show_recipe_list(request):
    return render(request, 'recipe/recipe_list.html')

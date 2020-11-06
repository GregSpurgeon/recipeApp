from django.shortcuts import render
from recipe_app.models import Author, Recipe
# Create your views here.
def home_page(request):
  home = "index.html"
  return render(request, home, {"recipes": Recipe.objects.all()})

def recipe_page(request, recipe_id):
  my_recipe = Recipe.objects.get(id=recipe_id)
  return render(request, 'recipe_detail.html', {"recipe": my_recipe})

def author_detail(request, author_id):
  my_author = Author.objects.get(id=author_id)
  return render(request, "author_detail.html", {"author":my_author})
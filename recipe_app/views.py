from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddRecipeForm, AddAuthorForm

# Create your views here.


def home_page(request):
    home = "index.html"
    return render(request, home,
                  {"recipes": Recipe.objects.all()})


def recipe_page(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {"recipe": my_recipe})


def add_recipe(request):
    html = "recipe_add_form.html"
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
              title=data['title'],
              author=data['author'],
              description=data['description'],
              time_requirment=data['time_requirment'],
              instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('recipe_page',
                                        kwargs={'recipe_id': new_recipe.id}))

    form = AddRecipeForm()
    return render(request, html, {'form': form})


def author_detail(request, author_id):
    my_author = Author.objects.get(id=author_id)
    return render(request, "author_detail.html", {"author": my_author})


def add_author(request):
    html = "author_add_form.html"
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_author = Author.objects.create(
              name=data['name'],
              bio=data['bio']
            )
            return HttpResponseRedirect(
              reverse('author_detail',
                      kwargs={'author_id': new_author.id})
            )

    form = AddAuthorForm()
    return render(request, html, {'form': form})

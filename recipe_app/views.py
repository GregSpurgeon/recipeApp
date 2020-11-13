from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def home_page(request):
    home = "index.html"
    return render(request, home,
                  {"recipes": Recipe.objects.all()})


def recipe_page(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {"recipe": my_recipe})


@login_required
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


@login_required
def add_author(request):
    if request.user.is_staff:
        html = "author_add_form.html"
        if request.method == 'POST':
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(
                  username=data['username'], password=data['password']
                )
                new_author = Author.objects.create(
                  name=data['name'],
                  bio=data['bio'],
                  user=new_user
                )
                return HttpResponseRedirect(
                  reverse('author_detail',
                          kwargs={'author_id': new_author.id})
                )
        form = AddAuthorForm()
        return render(request, html, {'form': form})
    return render(request, 'error_page.html')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home_page')))
    form = LoginForm()
    return render(request, 'author_add_form.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))

from django.shortcuts import render

from .models import Recipe, Ingredient
from .forms import RecipeCreationForm, IngredientCreationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import QuerySet, Q
from django.db.models import F
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.auth.decorators import login_required


def home_page_view(request: WSGIRequest):
    recipes = queryset_optimization(Recipe.objects.all())[:100]
    context: dict = {
        "recipes": recipes
    }
    # for note in notes:
    #     print(note["tags_list"])
    return render(request, "home.html", context)


def queryset_optimization(queryset: QuerySet) -> QuerySet:
    return (
        queryset
        .select_related("user")
        .prefetch_related("ingredients")
        .annotate(
            username=F('user__username'),
            # i_list=ArrayAgg("ingredients__name", distinct=True),
        )
        .values("name", "time_minutes", "created_at", "username")
        .distinct()
        .order_by("-created_at")
    )


@login_required
def create_recipe(request: WSGIRequest):
    form = RecipeCreationForm()

    if request.method == "POST":
        form = RecipeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("home"))
    return render(request, 'create-recipe.html', {'form': form})


@login_required
def create_ingredient(request: WSGIRequest):
    form = IngredientCreationForm()

    if request.method == "POST":
        form = IngredientCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save_m2m()
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'create-ingredient.html', {'form': form})


def about_us_page_view(request):
    return render(request, 'about_us.html')


def greetings_page_view(request: WSGIRequest):
    return render(request, "greeting.html")

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.handlers.wsgi import WSGIRequest
from .models import User
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def register_view(request: WSGIRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("lallalal")
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )

            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register.html', {'form': form})


@login_required
def show_user(request: WSGIRequest, username: str):
    user = User.objects.get(username=username)
    return render(request, 'show-user.html', {"user": user})


@login_required
def edit_user(request: WSGIRequest):
    user = User.objects.get(username=request.user.username)
    # if request.user != user:
    #     return HttpResponseForbidden("У вас нет доступа к аккаунту этого пользователя!")
    if request.method == 'GET':
        form = UserProfileForm()
        context = {
            "form": form,
            "user": request.user,
        }
        return render(request, "user_profile.html", context)
    elif request.method == "POST" and "confirm" in request.POST:
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # user.username = form.cleaned_data['username']
            if form.cleaned_data['first_name']:
                request.user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            return HttpResponseRedirect(reverse('show-profile', args=[request.user.username]))
        return render(request, 'user_profile.html', {'form': form})

"""
URL configuration for food_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app.views import home_page_view, about_us_page_view, greetings_page_view
from users.views import edit_user, show_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greetings_page_view, name="greeting"),
    path('account/', include("users.urls")),
    path('food/', include("main_app.urls")),
    path('main', home_page_view, name="home"),
    path('about_us', about_us_page_view, name="about-us"),
    path('profile/show_profile/<username>', show_user, name="show-profile"),
    path('profile/edit', edit_user, name="edit-profile"),

]

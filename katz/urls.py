from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from .views import logoutuser


# Import all methods from views.py
from . import views

# This is a list of the URL path names (webpages) and their corresponding "view" name.
# The view name is the name of the matching method from the views.py file.
urlpatterns = [
    path ('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kittens/', views.kittens, name='kittens'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('login_page/', views.login_page, name='login_page'),
    path('cat_register/', views.cat_register, name='cat_register'),
    path('logout/', logoutuser, name='logout'),
    path('query_test/', views.query_test, name='query_test'),



]
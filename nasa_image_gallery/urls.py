from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.auth import logout
urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('logout/', logout, name='logout'),
    

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path("accounts/", include("django.contrib.auth.urls")),

    path('exit/', views.index_page, name='exit'),
]
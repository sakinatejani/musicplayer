from django.urls import path

from . import views

app_name = "App"


urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('player/player/', views.player, name='player'),
        path('add_music/', views.added_player, name='music'),


]


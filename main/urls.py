from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('games', views.games,name='games'),
    path('blog', views.blog,name='blog'),
    path('user_agreement', views.user_agreement,name='user_agreement'),
    path('privacy_policy', views.privacy_policy,name='privacy_policy'),
    path('games/<name_game>', views.game,name='game'), 
]
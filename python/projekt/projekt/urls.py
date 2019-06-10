"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from excercise.userviews import RegView, user_loginview, profileview
from excercise.views import TirView, webtournamentview
from excercise.tournamentviews import quittournament, usertournamentsview, takepart,  AddTurnamentView, turnamentview, mytournamentsview, deletetournament


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tir',TirView.as_view()),
    path('login',user_loginview),
    path('register',RegView.as_view()),
    path('usertournaments', usertournamentsview),
    path('turnament',  turnamentview),
    path('addturnament',AddTurnamentView.as_view()),
    path('takepart',takepart),
    path('deletetournament',deletetournament),
    path('quittournament', quittournament),
    path('mytournaments', mytournamentsview),
    path('webtournament', webtournamentview),
    path('profile', profileview),
]

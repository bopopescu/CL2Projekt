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
from django.urls import path, re_path
from excercise.userviews import RegView, user_loginview, profileview
from excercise.views import TirView
from excercise.tournamentviews import quittournament, usertournamentsview, takepart,  AddTurnamentView, turnamentview, mytournamentsview, deletetournament, detaletournament, WebturnamentView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TirView.as_view()),
    path('login',user_loginview, name= 'login'),
    path('register',RegView.as_view(), name='register'),
    path('usertournaments', usertournamentsview, name='userturnament'),
    path('turnament',  turnamentview, name='tournament'),
    path('addturnament',AddTurnamentView.as_view(), name='addtournament'),
    re_path(r'^takepart/(?P<turnament_id>(\d+))/$',takepart, name='takepart'),
    path('deletetournament',deletetournament, name='deletetournament'),
    path('quittournament', quittournament, name='quittournament'),
    path('mytournaments', mytournamentsview, name='mytournament'),
    path('webturnament', WebturnamentView, name='webtournament'),
    path('profile', profileview, name='profile'),
    re_path (r'^detaletournament/(?P<turnament_id>(\d+))/$', detaletournament, name='detaletournament'),
]

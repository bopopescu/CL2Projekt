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
from django.urls import path,re_path
from excercise.views import TirView, turnamentview, RegView
from excercise.views import AddturnamentView,user_loginview,resignturnament, newturnamentview
from excercise.views import  userturnamentsview, takepart,profileview, addturnament, deleteturnament


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tir',TirView.as_view()),
    path('login',user_loginview),
    path('register',RegView.as_view()),
    path('userturnament', userturnamentsview),
    path('turnament',  turnamentview),
    path('addturnament',AddturnamentView.as_view()),
    path('takepart',takepart),
    path('deleteturnament',deleteturnament),
    path('addturnament',addturnament),
    path('resignturnament',resignturnament),
    path('newturnament',newturnamentview),
    path('profile', profileview),
]

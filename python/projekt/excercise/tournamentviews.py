from django.views import View
from .models import Turnament,Usertur
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from excercise.forms import AddForm, SignUpForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def turnamentview(request):
    turnament = Turnament.objects.all()
    turnaments_page = request.GET.get('recipe_page')
    paginator = Paginator(turnament, 5)
    try:
        turnaments_page = paginator.page(turnaments_page)
    except PageNotAnInteger:
        turnaments_page = paginator.page(request.GET.get('page', 1))
    except EmptyPage:
        turnaments_page = paginator.page(paginator.num_pages)
    return render(request, 'turnieje.html', {'turnaments_paginator': turnaments_page})

class AddturnamentView(View):
    def get(self,request):
        form = AddForm()
        return render(request, 'addturnament.html', {'form':form})
    def post(self, request):
        form = AddForm(request.POST)
        print("AddturnamentView", form.is_valid())
        if form.is_valid():
            a1 = form.cleaned_data['name']
            a2 = form.cleaned_data['place']
            a3 = form.cleaned_data['date_start']
            a4 = form.cleaned_data['date_end']
            a5 = form.cleaned_data['price']
            a6 = form.cleaned_data['description']
            turnament = Turnament.objects.create(
                name=a1,
                place=a2,
                date_start=a3,
                date_end=a4,
                price= a5,
                description = a6,
                user = request.user)
            turnament.save()
            return redirect('/mytournaments')
        else:
            return render(request, 'addturnament.html', {'form': form})






@login_required
def userturnamentsview(request):
    if request.method =='GET':
        userturnaments = Usertur.objects.filter(user=request.user).order_by('-id')
        tournaments = [usertur.tournament for usertur in userturnaments]
        tournaments_page = request.GET.get('page')
        paginator = Paginator(tournaments, 5)
        try:
            tournaments_page = paginator.page(tournaments_page)
        except PageNotAnInteger:
            tournaments_page = paginator.page(request.GET.get('page', 1))
        except EmptyPage:
            tournaments_page = paginator.page(paginator.num_pages)
        return render(request, 'userturnaments.html', {'turnaments_paginator': tournaments_page, 'turnaments':userturnaments})


@login_required
def takepart(request):
    if request.method=='GET':
        turnamentId = request.GET.get('turnamentId')
        Usertur.objects.get_or_create(user=request.user, tournament_id=turnamentId)
        return redirect("/userturnaments")



@login_required
def quittournament(request):
    if request.method=='GET':
        tournament_id = request.GET.get('tournamentId')
        Usertur.objects.get( tournament_id = tournament_id, user=request.user).delete()

        return redirect("/userturnaments")

@login_required
def mytournamentsview(request):
    if request.method =='GET':
        mytournaments = Turnament.objects.filter(user=request.user)
        tournaments_page = request.GET.get('page')
        paginator = Paginator(mytournaments, 5)
        try:
            tournaments_page = paginator.page(tournaments_page)
        except PageNotAnInteger:
            tournaments_page = paginator.page(request.GET.get('page', 1))
        except EmptyPage:
            tournaments_page = paginator.page(paginator.num_pages)
        return render(request, 'mytournaments.html', {'tournaments_paginator': tournaments_page, 'tournaments':mytournaments})

@login_required
def deletetournament(request):
    if request.method=='GET':
        tournament_id= request.GET.get('tournamentId')
        Turnament.objects.filter( id=tournament_id).delete()
        return redirect("/mytournaments")
from django.views import View
from .models import Turnament, Usertur
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from excercise.forms import AddForm, GradeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
@login_required
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


class AddTurnamentView(View):
    @method_decorator(login_required)
    def get (self,request):
        if request.method =='GET':
            form = AddForm()
            return render(request, 'addturnament.html', {'form':form})
    @method_decorator(login_required)
    def post(self,request):
        form = AddForm(request.POST)
        print("addturnamentsview", form.is_valid())
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
def usertournamentsview(request):
    if request.method == 'GET':
        user_tournaments = Usertur.objects.filter(user=request.user).order_by('-id')
        tournaments = [usertur.tournament for usertur in user_tournaments]
        tournaments_page_num = request.GET.get('page')
        paginator = Paginator(tournaments, 5)
        try:
            tournaments_page = paginator.page(tournaments_page_num)
        except PageNotAnInteger:
            tournaments_page = paginator.page(request.GET.get('page', 1))
        except EmptyPage:
            tournaments_page = paginator.page(paginator.num_pages)
        return render(request, 'usertournaments.html',
                      {'tournaments_paginator': tournaments_page, 'tournaments': user_tournaments})


@login_required
def takepart(request, turnament_id):
    if request.method=='GET':
        Usertur.objects.get_or_create(user=request.user, tournament_id=turnament_id)
        return redirect("/detaletournament/"+turnament_id)



@login_required
def quittournament(request):
    if request.method=='GET':
        tournament_id = request.GET.get('tournamentId')
        Usertur.objects.get( tournament_id = tournament_id, user=request.user).delete()

        return redirect("/usertournaments")

@login_required
def mytournamentsview(request):
    if request.method =='GET':
        mytournaments = Turnament.objects.filter(user=request.user)
        tournaments_page_num = request.GET.get('page')
        paginator = Paginator(mytournaments, 5)
        try:
            tournaments_page = paginator.page(tournaments_page_num)
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

@login_required
def detaletournament(request, turnament_id):
    if request.method=='GET':
        turnament = Turnament.objects.get(id=turnament_id)
        usertournament = None
        try:
            usertournament = Usertur.objects.get(user=request.user, turnament_id=turnament_id)
        except:
            pass
        return render(request,"webturnament.html", {'turnament':turnament, 'userturnament':usertournament})

class WebturnamentView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.method == 'GET':
            webform = GradeForm()
            return render(request, 'webturnament.html', {'form': webform})
    @method_decorator(login_required)
    def post(self, request):
        webform = GradeForm(request.POST)
        if webform.is_valid():
            a7 = webform.cleaned_data['grade']
            grade = Turnament.objects.get(
                grade=a7,
                user=request.user)
            grade.save()
            return redirect('/webturnament')
        else:
            return render(request, 'webturnament.html', {'form': webform})



@login_required
def quittournament(request):
    if request.method=='GET':
        tournament_id = request.GET.get('tournamentId')
        Usertur.objects.get( tournament_id = tournament_id, user=request.user).delete()

        return redirect("/usertournaments")
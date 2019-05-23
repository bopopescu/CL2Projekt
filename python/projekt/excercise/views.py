from django.views import View
from .models import Turnament,Usertur
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from excercise.forms import AddForm, SignUpForm #UserForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class TirView(View):
    def get(self,request):
        three_rturnaments = Turnament.objects.all().order_by('?')[:3]
        return render(request, "base.html", { 'turnaments': three_rturnaments })

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
                description = a6)
            turnament.save()
            return redirect('/newturnament')
        else:
            return render(request, 'addturnament.html', {'form': form})





@login_required
def special(request):
    return render (request, 'profile{}'.format(user.id))

@login_required
def user_logout(request):
    logout(request)
    return render(request ('tir'))

class RegView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'rejestracja.html', {'form': form})
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            a1 = form.cleaned_data['username']
            a2 = form.cleaned_data['password1']
            a3 = form.cleaned_data['email']
            if not User.objects.filter(email=a3).exists():
                user = User.objects.create_user(
                username=a1,
                password=a2,
                email=a3)
                user.save()
                request.session['userid'] = user.id
                return redirect('/profile')
        else:
            form = SignUpForm(request.POST)
            return render(request, 'rejestracja.html', {'form': form})


def profileview(request):
    userid = request.session.get('userid', False)
    user1 = User.objects.get(id=userid)
    return render(request,'profile.html', {'username': user1.username, 'email': user1.email})


def user_loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user, username, password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['userid'] = user.id
                return redirect('/profile')
            else:
                return HttpResponse('Nie poprawne dane')
        else:
            return render(request, 'logowanie.html')

    return render(request, 'logowanie.html')

@login_required
def userturnamentsview(request):
    if request.method =='GET':
        userturnament = Usertur.objects.filter(user=request.user)
        turnaments = [usertur.tournament for usertur in userturnament]
        turnaments_page = request.GET.get('recipe_page')
        paginator = Paginator(turnaments, 5)
        try:
            turnaments_page = paginator.page(turnaments_page)
        except PageNotAnInteger:
            turnaments_page = paginator.page(request.GET.get('page', 1))
        except EmptyPage:
            turnaments_page = paginator.page(paginator.num_pages)
        return render(request, 'userturnament.html', {'turnaments_paginator': turnaments_page, 'turnaments':userturnament})


@login_required
def takepart(request):
    if request.method=='GET':
        turnamentId = request.GET.get('turnamentId')
        Usertur.objects.get_or_create(user=request.user, tournament_id=turnamentId)
        userturnament = Usertur.objects.filter(user=request.user)
        turnaments = [usertur.tournament for usertur in userturnament]
        print(userturnament)
        return render(request,'turnieje.html',{'turnaments': turnaments})

@login_required
def addturnament(request):
    if request.method=='GET':
        turnamentId = request.GET.get('turnamentId')
        Usertur.objects.get_or_create(user=request.user, tournament_id=turnamentId)
        userturnament = Usertur.objects.filter(user=request.user)
        turnaments = [usertur.tournament for usertur in userturnament]
        print(userturnament)
        return render(request,'newturnament.html',{'turnaments': turnaments})

@login_required
def resignturnament(request):
    if request.method=='GET':
        turnamentname = request.GET.get('turnamentname')
        Usertur.objects.filter( tournament_id=turnamentname).delete()
        userturnament = Usertur.objects.filter(user=request.user)
        turnaments = [usertur.tournament for usertur in userturnament]
        return render(request,'userturnament.html',{'turnaments': turnaments})

@login_required
def deleteturnament(request):
    if request.method=='GET':
        turnamentname= request.GET.get('turnamentname')
        Turnament.objects.filter( id=turnamentname).delete()
        turnament = Turnament.objects.filter(name=request.name)
        turnaments = [turnament.tournament for turnament in turnament]
        return render(request,'newturnament.html',{'turnaments': turnaments})

@login_required
def newturnamentview(request):
    if request.method =='GET':
        newturnament = Usertur.objects.filter(user=request.user)
        turnaments = [usertur.tournament for usertur in newturnament]
        turnaments_page = request.GET.get('recipe_page')
        paginator = Paginator(turnaments, 5)
        try:
            turnaments_page = paginator.page(turnaments_page)
        except PageNotAnInteger:
            turnaments_page = paginator.page(request.GET.get('page', 1))
        except EmptyPage:
            turnaments_page = paginator.page(paginator.num_pages)
        return render(request, 'newturnament.html', {'turnaments_paginator': turnaments_page, 'turnaments':newturnament})
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
class TirView(View):
    def get(self,request):
        three_rturnaments = Turnament.objects.all().order_by('?')[:3]
        return render(request, "base.html", { 'turnaments': three_rturnaments })




@login_required
def deleteturnament(request):
    if request.method=='GET':
        turnamentId= request.GET.get('turnamentId')
        Turnament.objects.filter( id=turnamentId).delete()
        return redirect("/mytournaments")



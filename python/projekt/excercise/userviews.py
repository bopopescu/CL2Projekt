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

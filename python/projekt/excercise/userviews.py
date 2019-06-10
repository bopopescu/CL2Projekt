from django.views import View
from django.shortcuts import redirect
from excercise.forms import  SignUpForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

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
        if not form.is_valid():
            return render(request, 'rejestracja.html', {'form': form})
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        email = form.cleaned_data['email']

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email)
        user.save()
        authenticate(username=username, password=password)
        login(request, user)
        return redirect('/profile')

@login_required
def profileview(request):
    user1 = request.user
    return render(request,'profile.html', {'username': user1.username, 'email': user1.email})

@login_required
def user_loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['userid'] = user.id
                return redirect('/profile')
            else:
                return HttpResponse(_('Nie poprawne dane'))
        else:
            return render(request, 'logowanie.html')

    return render(request, 'logowanie.html')

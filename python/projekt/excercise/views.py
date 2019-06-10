from django.views import View
from .models import Turnament
from django.shortcuts import render

class TirView(View):
    def get(self,request):
        three_rturnaments = Turnament.objects.all().order_by('?')[:3]
        return render(request, "base.html", { 'turnaments': three_rturnaments })

def webtournamentview(request):
    if request.method=='GET':
        return render(request,"webturnament.html")



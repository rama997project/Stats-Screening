from django.shortcuts import render
from django.http import HttpResponse
from PortfolioScreen.models import Stock


def PortfolioScreen(request):
    context = {
        'Stocks': Stock.objects.all()
    }
    return render(request, 'PortfolioScreen/main.html', context)

def about(request):
    return render(request, 'PortfolioScreen/about.html', {'title:':'About'})
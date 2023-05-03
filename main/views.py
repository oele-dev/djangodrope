from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def index(request):
    latest_portfolios = Portfolio.objects.order_by("-publish_at")[:6]
    context = {"latest_portfolios": latest_portfolios}
    return render(request, "public/index.html", context)

def left(request):
    context = {}
    return render(request, "public/left.html", context)
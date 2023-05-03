from django.shortcuts import render, get_object_or_404

from .models import Portfolio, Post


# Create your views here.
def index(request):
    portfolios = Portfolio.objects.order_by("-publish_at")[:6]
    posts = Post.objects.order_by('-publish_at')[:2]
    context = {
        "portfolios": portfolios,
        "posts": posts
        }
    return render(request, "public/index.html", context)

def left(request):
    context = {}
    return render(request, "public/left.html", context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "public/detail.html", {"post": post})

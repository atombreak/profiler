from django.shortcuts import render

from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {"posts":posts})
    
def gallery(request):
    return render(request, 'gallery.html')
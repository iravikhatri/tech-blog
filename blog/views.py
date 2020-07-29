from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context) 

def work(request):
    context = {
        'title': "Work"
    }
    return render(request, 'blog/work.html', context)

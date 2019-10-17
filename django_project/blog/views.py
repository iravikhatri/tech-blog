from django.shortcuts import render

posts = [
    {
        "author": "Ravi Khatri",
        "title": "First Post 1",
        "content": "Fisrt Blog Content",
        "date_posted": "17 Oct 2019"
    },
    {
        "author": "Price Khatri",
        "title": "Second Post 2",
        "content": "Second Blog Content",
        "date_posted": "18 Oct 2019"
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)

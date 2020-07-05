from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    print(dict(request.POST))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password, user,'----------------->')

        if user is not None:
            login(request, user)
            print('user logged in','----------------->')
            return redirect('blog-home')
        else:
            messages.success(request, f"Your username or password is incorrect, Please try again.")
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('blog-home')

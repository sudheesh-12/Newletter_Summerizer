from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .utils import function1, function2, function3

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Logged in successfully!')
        else:
            return HttpResponse('Invalid credentials')

    return render(request, 'login.html')

def home(request):
    context = {
        'result1': function1(),
        'result2': function2(),
        'result3': function3(),
    }
    return render(request, 'home.html', context)
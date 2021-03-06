from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.


def index(request):
    return redirect('/tils')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user, backend ='django.contrib.auth.backends.ModelBackend')
            return redirect('/posts/list')
    else:
        form = UserForm()
    return render(request, 'authentication/signup.html', {'form' : form})
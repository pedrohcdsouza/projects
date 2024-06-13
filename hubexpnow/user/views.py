from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import string

def temporary_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return get_random_string(8, characters)

def create(request):
    if request.method == 'GET':
        return render(request, 'user/pages/create.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        userexits = User.objects.filter(username=username).first()

        if userexits:
            return HttpResponse('já existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse('login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'user/pages/login.html')
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)
            
            return render(request, 'user/pages/login.html')
        else:
            return HttpResponse('Usuário ou senha inválido')

@login_required()
def logout(request):
    logout_django(request)
    return redirect(reverse('login'))
    
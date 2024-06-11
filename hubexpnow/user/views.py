from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.utils.crypto import get_random_string
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
        password = temporary_password()
        HttpResponse('username')

        userexits = User.objects.filter(username=username).first()

        if userexits:
            return HttpResponse('já existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return HttpResponse(f'Usuário cadastrado com sucesso. Sua senha temporaria: {password}')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/pages/login.html')
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Usuário ou senha inválido')
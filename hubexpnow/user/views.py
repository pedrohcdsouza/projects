from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

def register_get(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'user/pages/register.html', {
        'form': form,
    })

def register_post(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado com sucesso.')

        del(request.session['register_form_data'])


    return redirect('user:register')

def login_get(request):
    form = LoginForm()
    return render(request, 'user/pages/login.html', {
        'form': form,
        'form_action': reverse('user:login_post')
    })

def login_post(request):
    if not request.POST:
        raise Http404
    
    form = LoginForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username',''),
            password=form.cleaned_data.get('password',''),
        )
        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Usuário e/ou senha inválidas.')
    else:
        messages.error(request, 'Erro ao validar formulário.')
    return redirect(reverse('user:login'))
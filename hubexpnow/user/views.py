from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404
from django.contrib import messages

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
    return render(request, 'user/pages/login.html')

def login_post(request):
    return render(request, 'user/pages/login.html')
from django.shortcuts import render
from .forms import RegisterForm
from django.http import Http404

def create(request):
        form = RegisterForm()
        return render(request, 'user/pages/create.html', {
            'form': form,
        })
    
def create_post(request):
        if not request.POST:
            raise Http404()
        form = RegisterForm(request.POST)
        return render(request, 'user/pages/create.html', {
            'form': form,
        })
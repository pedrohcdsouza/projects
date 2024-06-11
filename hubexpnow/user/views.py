from django.shortcuts import render

def create(request):
    return render(request, 'user/pages/create.html')

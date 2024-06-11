from django.shortcuts import render

def manager(request):
    return render(request, 'manager/pages/manager.html')
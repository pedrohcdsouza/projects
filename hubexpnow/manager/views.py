from django.shortcuts import render
from .decorators import group_required

@group_required('analysts')
def manager(request):
    return render(request, 'manager/pages/manager.html')
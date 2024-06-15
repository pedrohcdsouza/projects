from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .decorators import group_required
from django.contrib.auth.models import Group

@group_required('analysts')
def manager(request):
    clients_group = Group.objects.get(name='clients')
    clients = clients_group.user_set.all()

    context = {
        'clients': clients,
    }
    return render(request, 'manager/pages/manager.html', context)

@group_required('analysts')
def manager_client(request, username):
    client = get_object_or_404(User, username=username)

    context = {
        'client': client,
    }
    return render(request, 'manager/pages/manager_client.html', context)
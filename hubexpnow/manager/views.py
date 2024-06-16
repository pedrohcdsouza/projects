from django.shortcuts import render
from manager.decorators import group_required
from django.contrib.auth.models import Group

@group_required('analysts')
def manager(request):
    clients_group = Group.objects.get(name='clients')
    clients = clients_group.user_set.all()

    context = {
        'clients': clients,
    }
    return render(request, 'manager/pages/manager.html', context)
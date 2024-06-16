from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from manager.decorators import group_required
from django.contrib.auth.models import Group

@group_required('analysts')
def user_page(request, username):
    client = get_object_or_404(User, username=username)

    context = {
        'client': client,
    }
    return render(request, 'manager/pages/user_page.html', context)
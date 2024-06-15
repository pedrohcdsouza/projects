from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager, name='manager'),
    path('cliente/<str:username>/', views.manager_client, name='manager_client'), 
    # path('<str:username>/edit/', views.edit_client, name='edit_client'),
    # path('<str:username>/delete/', views.delete_client, name='delete_client'),
]
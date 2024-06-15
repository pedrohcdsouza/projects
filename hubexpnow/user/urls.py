from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_get, name='register_get'),
    path('register/post', views.register_post, name='register_post'),
]

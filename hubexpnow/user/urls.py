from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_get, name='register_get'),
    path('register/post/', views.register_post, name='register_post'),
    path('login/', views.login_get, name='login_get'),
    path('login/post/', views.login_post, name='login_post'),
    path('logout/', views.logout_get, name='logout_get'),

]

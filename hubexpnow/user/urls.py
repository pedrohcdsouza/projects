from django.urls import path
from . import auth_views, user_views

app_name = 'user'

urlpatterns = [
    path('register/', auth_views.register_get, name='register_get'),
    path('register/post/', auth_views.register_post, name='register_post'),
    path('login/', auth_views.login_get, name='login_get'),
    path('login/post/', auth_views.login_post, name='login_post'),
    path('logout/', auth_views.logout_get, name='logout_get'),
    path('<str:username>/', user_views.user_page, name='user_page')
]
from django.urls import path
from account import views
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from account.forms import UserForm

app_name = 'acc'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

from django.urls import path
from account import views

urlpatterns=[
    
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    

]
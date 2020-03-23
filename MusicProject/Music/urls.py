from django.urls import path
from Music import views

urlpatterns = [
    path('', views.index, name='index')
]

from django.urls import path
from . import views

app_name = 'register2'

urlpatterns = [
    path('signin/', views.signIn, name='signin')
]
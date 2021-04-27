from django.urls import path
from . import views
urlpatterns = [
    path('', views.blogabout, name= 'About'),
]
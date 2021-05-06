from django.shortcuts import render, redirect
from .form import UserForm
# Create your views here.
def signIn(request):
    form = UserForm()
   
    context = {
        "form": form
    }
    success_url = reverse_lazy('home')

    return render(request, 'register2/signin.html', context)
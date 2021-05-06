from django.shortcuts import render,redirect
from .form import UserForm
# Create your views here.
def signUp(request):
    form = UserForm()
    if request.method == "POST":
        # firstname = request.get['firstname']
        form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/register2/signin')
    context = {
        "form": form
    }
    return render(request, 'register/signup.html', context)
    

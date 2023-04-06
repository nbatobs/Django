from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
<<<<<<< HEAD
from .forms import SignUpForm
=======
>>>>>>> 96b17488572a68bfdecc38fc3f7f361340ccc592
# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in !")
            return redirect('home')
        else:
            messages.success(request,"error logging in, try again")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
<<<<<<< HEAD
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request,'You Have Successfully Registered')
            return redirect('home')
    else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form': form})
=======
    return redirect('home')
>>>>>>> 96b17488572a68bfdecc38fc3f7f361340ccc592

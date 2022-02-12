from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, UserForm, UserProfileForm
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {'userprofile': userprofile}
    return render(request, 'accounts/dashboard.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = SignupForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'accounts/signup.html', context)


def logout(request):
    return render(request, 'accounts/logout.html')


def forgetPassword(request):
    return render(request, 'accounts/forgetPassword.html')

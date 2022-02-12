from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {'userprofile': userprofile}
    return render(request, 'accounts/dashboard.html', context)

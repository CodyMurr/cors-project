from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, UserProfile
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, UserForm, UserProfileForm
from django.http import HttpResponse

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.


@login_required
def dashboard(request):
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {'userprofile': userprofile}
    return render(request, 'accounts/dashboard.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            url = request.META.get('HTTP_REFERER')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            # This will add the user to the database
            user.save()

            # create a new user profile
            profile = UserProfile()
            profile_user_id = user.id
            profile.profile_picture = 'default/default-user.png'
            profile.save()

            # activate the user
            current_site = get_current_site(request)
            mail_subject = "Hello beautiful, activate your account"
            msg = render_to_string('accounts/verify_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, msg, to=[to_email])
            send_email.send()
            # This is how we log a user in via code
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = SignupForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'accounts/signup.html', context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request):
    user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.sucess(request, "Congratulations! Your account is activated.")
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('signup')


def forgetPassword(request):
    return render(request, 'accounts/forgetPassword.html')

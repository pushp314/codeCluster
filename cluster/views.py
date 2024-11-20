from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *



# Create your views here.
def home(request):
    contest = Contest.objects.all()
    if request.user.is_authenticated:
        register = Registration.objects.filter(user=request.user).first()
    else:
        register = None  # No registration if the user is not authenticated

    return render(request, 'index.html', {'register': register, 'contest':contest}, )

# Signin view for login functionality
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('home')  
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user with email
            auth_login(request, user)  # Log in the user automatically
            return redirect('home')  # Redirect to home page
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user  # Link the registration to the logged-in user
            registration.save()
            messages.success(request, "Registration submitted successfully!")
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')




@login_required
def registration_status(request):
    try:
        registration = Registration.objects.get(user=request.user)
        if registration.status == 'Approved':
            messages.success(request, "Congratulations! Your registration has been approved.")
        status = registration.status
    except Registration.DoesNotExist:
        registration = None
        status = "Not Registered"
    
    return render(request, 'registration_status.html', {'registration': registration, 'status': status})



@login_required
def profile(request):
    try:
        registration = Registration.objects.get(user=request.user)
    except Registration.DoesNotExist:
        registration = None

    return render(request, 'dashboard/profile.html', {'registration': registration})


def about(request):
    return render(request, 'pages/about.html')

def terms(request):
    return render(request, 'pages/terms.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save the form data to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        return redirect('contact')  # Redirect to the same page after form submission

    return render(request, "pages/contactus.html")  # Render your form template



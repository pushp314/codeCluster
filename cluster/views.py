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


# Signup view for registration functionality
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            auth_login(request, user)  # Log the user in automatically after signup
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()

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



from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

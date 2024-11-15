from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),  # Custom signup view
    path('login/', signin, name='login'),  # Use the custom signin view
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout view with redirect to home
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
    path('registration_status/', registration_status, name='status'),
    path('about/', about, name='about'),
]

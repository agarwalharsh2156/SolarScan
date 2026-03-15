from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(next_page = 'profile'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
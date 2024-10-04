from django.urls import path
from account.views import UserRegistrationView, UserLoginView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-Login'),
      path('logout/',LogoutView.as_view(),name='logout'),
]

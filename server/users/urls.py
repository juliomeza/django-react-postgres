from django.urls import path
from .views import LoginView, LogoutView, AuthStatusView, TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('auth-status/', AuthStatusView.as_view(), name='auth-status'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
from django.urls import path 
from .views import SignupView, VerifySignupView, ForgotPasswordView, PasswordResetView, UserObtainView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup-user"),
    path('verify/<str:token>/', VerifySignupView.as_view(), name="verify-user"),
    path('forgotpassword/', ForgotPasswordView.as_view(), name="forgot-password"),
    path('resetpassword/<str:token>/', PasswordResetView.as_view(), name="reset-password"),
    
    path('signin/', TokenObtainPairView.as_view(), name='signin-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('detail/', UserObtainView.as_view(), name='user-info'),
]
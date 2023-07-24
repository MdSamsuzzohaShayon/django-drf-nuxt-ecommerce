import jwt
import os
import logging

from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignupSerializer, PasswordForgotSerializer, PasswordResetSerializer, CustomTokenObtainPairSerializer
from .models import User
from . import emails
from drfecom.keys import TokenTypes

"""
Used for create-only endpoints. Provides a post method handler.
"""
class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs): # Use perform_create instead from serializer
        user_instance = None
        user_email = request.data.get('email')
        try:
            user_instance = User.objects.get(email=user_email)
            if user_instance.is_active:
                return Response({'message': 'This account is already verified, now you can use this account!'}, status=status.HTTP_208_ALREADY_REPORTED) 
        except Exception:
            pass

        serializer = None
        if user_instance is not None:
            serializer = SignupSerializer(user_instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save(is_active = False)

            payload = {
                "type": TokenTypes.REGISTER.value,
                "email": user_email,
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=20)
            }

            encoded_token = jwt.encode(payload, os.getenv('JSON_TOKEN_SECRET'), algorithm="HS256")

            emails.SendEmail.send_signup_confirmation(request, user, encoded_token)
            return Response({'message': 'a verification url is been sent to your email'}, status=status.HTTP_201_CREATED) 

        return Response({'message': 'Provide valid data in order to '}, status=status.HTTP_406_NOT_ACCEPTABLE) 
    

class VerifySignupView(GenericAPIView):
    def put(self, request, token):
        try:
            decoded_token = jwt.decode(token, os.getenv('JSON_TOKEN_SECRET'), algorithms=["HS256"])
            if decoded_token['type'] != TokenTypes.REGISTER.value:
                return Response({'message': 'Invalid token'}, status=status.HTTP_406_NOT_ACCEPTABLE)                 
            
            user_instance = User.objects.get(email=decoded_token['email'])
            if user_instance is None:
                return Response({'message': 'No user registered, with this email'}, status=status.HTTP_406_NOT_ACCEPTABLE)                 
            if user_instance.is_active:
                return Response({'message': 'Account already activated.'}, status=status.HTTP_208_ALREADY_REPORTED)
            
            user_instance.is_active = True 
            user_instance.save()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError:
            return Response({'message': 'The token had been expired'}, status=status.HTTP_406_NOT_ACCEPTABLE) 
        except Exception as e:
            logging.error(e)
            return Response({'message': str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)  
        

class ForgotPasswordView(GenericAPIView):
    serializer_class = PasswordForgotSerializer
    
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        user_email = user.email

        payload = {
                "type": TokenTypes.RESET_PASSWORD.value,
                "email": user_email,
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=20)
            }
        encoded_token = jwt.encode(payload, os.getenv('JSON_TOKEN_SECRET'), algorithm="HS256")
        
        emails.SendEmail.send_reset_password_email(request=request, user_email=user_email, token=encoded_token)
        return Response({'detail': 'Password reset email sent.'}, status=status.HTTP_200_OK)


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'token': kwargs.get('token')}) # Generic views - Returns a serializer instance.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password has been reset.'}, status=status.HTTP_200_OK)
    

class SigninTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



        















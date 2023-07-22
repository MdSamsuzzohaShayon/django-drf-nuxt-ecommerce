from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.core.mail import EmailMultiAlternatives
from .serializers import SignupSerializer
from . import emails

# Create your views here.
# class SignupView(CreateAPIView):
#     serializer_class = serializers.SignupSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():

#             # create a new user and deactivate the user until the email is confirmed
#             user = serializer.save(is_active=False)

#             # Generate a unique token for the user
#             token = Token.objects.get_or_create(user=user)

#             # Send confirmation email
#             email.SendEmail.send_signup_confirmation(request, user, token)

#             return Response(
#                 {'Confirm email': 'Please check your email to confirm your address'},
#                 status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Used for create-only endpoints. Provides a post method handler.
"""
class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs): # Use perform_create instead
        serializer = self.get_serializer(data=request.data)
        print("request.data ", request.data)
        print("serializer.is_valid()", serializer.is_valid())
        if serializer.is_valid():
            user = serializer.save(is_active = False)
            print(user)

            subject, from_email, to = "hello", "mdsamsuzzoha5222@gmail.com", "mdshayon0@gmail.com"
            text_content = "This is an important message."
            html_content = "<p>This is an <strong>important</strong> message.</p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print("Sent email")
            # Generat token
            # Send token via email
            # email.SendEmail.send_signup_confirmation(request, user, token)
            emails.SendEmail.send_signup_confirmation(request, user, "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")

        return Response({'message': 'Please check your email to confirm your address'}, status=status.HTTP_201_CREATED) 

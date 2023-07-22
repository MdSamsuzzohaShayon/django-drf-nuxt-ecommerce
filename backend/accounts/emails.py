

#     @classmethod
#     def send_password_reset(cls, request, user, token):

#         # Generate the URL for the password reset link
#         password_reset_url = request.build_absolute_uri(reverse('password_reset_confirm', args=[str(token.key)]))

#         message = f'Hi {user.username},' \
#                   f'\n\nYou recently requested to reset your password for your account at {password_reset_url}.'
#         cls.send(
#             subject='Password reset request',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#             message=message,
#         )

#     @classmethod
#     def send_change_password(cls, user):
#         message = f'Hi {user.username}, your password has been changed successfully.'
#         cls.send(
#             subject='Password changed',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#             message=message,
#         )

#     @classmethod
#     def send_change_email(cls, new_email):
#         cls.send(
#             subject="Email Change Confirmation",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[new_email],
#             message=f"Your email has been changed to {new_email}.",
#         )




import logging
import os
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

"""
Although Python provides a mail sending interface via the smtplib module, Django provides a couple of light wrappers over it. 
https://docs.djangoproject.com/en/4.2/topics/email/
@classmethod Transform a method into a class method. -> https://docs.python.org/3/library/functions.html?highlight=property#classmethod
decorators in the standard library, -> https://wiki.python.org/moin/Decorators
"""

class SendEmail:

    @classmethod
    def send_message(cls, subject, recipient_list, text="", html_content=None):
        try:
            from_email = settings.EMAIL_HOST_USER
            email = EmailMultiAlternatives(subject, text, from_email, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)
        except Exception as e:
            logging.error(e)
            raise Exception('Failed to send email: {str(e)}')
        
    @classmethod 
    def send_signup_confirmation(cls, request, user, token):
        frontend_url = os.getenv("FRONTEND_URL")
        # to = user.email
        to = "mdshayon0@gmail.com"
        # first_token = token[0]
        first_token = token
        email_verify_url = f"{frontend_url}/user/verify/{first_token}"
        subject = "Confirm your email address"

        html_content = f"<div>" \
                            f"<h1>Email Verification<h1/>" \
                            f"<p>Shakil Furniture</p>" \
                            f"<br />" \
                            f"<br />" \
                            f"<a href='{email_verify_url}'>Verify</a>" \
                            f"<br />" \
                            f"<p>If the link does not work copy and link below and paste it in the browser!</p>" \
                            f"<p>{email_verify_url}</p>" \
                        f"</div>"
        
        cls.send_message(subject, recipient_list=[to], text="", html_content=html_content)
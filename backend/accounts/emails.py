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
            raise Exception(f'Failed to send email: {str(e)}')
        
    @classmethod 
    def send_signup_confirmation(cls, request, user_email, token):
        frontend_url = os.getenv("FRONTEND_URL")
        # to = user.email
        recipient_list = [user_email, 'mdsamsuzzoha5222@gmail.com']
        # first_token = token[0]
        first_token = token
        email_verify_url = f"{frontend_url}/user/verify/{first_token}"
        subject = "Confirm your email address"

        
        html_content =  f'<div style="width:100%; color:#2b2e30;">' \
                            f'<div class="section-1" style="text-align:center;">' \
                                f'<h1>Email Veriication</h1>' \
                                f'<p>Shakil urniture</p>' \
                            f'</div>' \
                            f'<br />' \
                            f'<br />' \
                            f'<div class="section-2" style="text-align:center; background: #2b2e30; width:100%; color: white; height: fit-content; padding: 50px 0;">' \
                                f'<a style="background:#235275; padding: 10px 20px; color:white; text-decoration: none; font-size: 1.5rem; weight:700;" href="{email_verify_url}">Verify</a>' \
                                f'<p style="color: white;">If the link does not work copy and link below and paste it in the browser!</p>' \
                                f'<p style="color: white;">{email_verify_url}</p>' \
                            f'</div>' \
                        f'</div>' 
        
        cls.send_message(subject, recipient_list=recipient_list, text="", html_content=html_content)

    @classmethod 
    def send_reset_password_email(cls, request, user_email, token):
        frontend_url = os.getenv("FRONTEND_URL")
        recipient_list = [user_email, 'mdsamsuzzoha5222@gmail.com']
        reset_password_url = f"{frontend_url}/user/reset/{token}"
        subject = "Reset your password"

        
        html_content =  f'<div style="width:100%; color:#2b2e30;">' \
                            f'<div class="section-1" style="text-align:center;">' \
                                f'<h1>Password Reset</h1>' \
                                f'<p>Shakil furniture</p>' \
                            f'</div>' \
                            f'<br />' \
                            f'<br />' \
                            f'<div class="section-2" style="text-align:center; background: #2b2e30; width:100%; color: white; height: fit-content; padding: 50px 0;">' \
                                f'<a style="background:#235275; padding: 10px 20px; color:white; text-decoration: none; font-size: 1.5rem; weight:700;" href="{reset_password_url}">Reset</a>' \
                                f'<p style="color: white;">If the link does not work copy and link below and paste it in the browser!</p>' \
                                f'<p style="color: white;">{reset_password_url}</p>' \
                            f'</div>' \
                        f'</div>' 
        
        cls.send_message(subject, recipient_list=recipient_list, text="", html_content=html_content)
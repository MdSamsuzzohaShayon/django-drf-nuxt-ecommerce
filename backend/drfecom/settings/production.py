from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SUPABASE_DB_NAME'),
        'USER': os.environ.get('SUPABASE_DB_USER'),
        'PASSWORD': os.environ.get('SUPABASE_DB_PASSWORD'),
        'HOST': os.environ.get('SUPABASE_DB_HOST'),
        'PORT': os.environ.get('SUPABASE_DB_PORT'),
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'your_smtp_host'
# EMAIL_PORT = 587  # The port for your SMTP server (usually 587 for TLS)
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@example.com'  # Your email address
# EMAIL_HOST_PASSWORD = 'your_email_password'  # Your email password
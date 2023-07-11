import os
import sys
from django.core.management import execute_from_command_line

def run_django_project():
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfecom.settings.base')

    # Execute the Django project
    # execute_from_command_line(sys.argv)
    execute_from_command_line(['manage.py', 'runserver'])

if __name__ == '__main__':
    run_django_project()
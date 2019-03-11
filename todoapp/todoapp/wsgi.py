"""
WSGI config for todoapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'todoapp.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoapp.settings")

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoapp.settings")

application = get_wsgi_application()

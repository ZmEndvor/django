"""
WSGI config for m project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys
from os.path import join, dirname, abspath
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)))

sys.path.insert(0, os.path.join(PROJECT_DIR,'../../..','vcmt/lib/python3.6/site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "m.settings")

application = get_wsgi_application()

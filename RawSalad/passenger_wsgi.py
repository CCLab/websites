import sys, os
INTERP = "/bin/python-2.6.1/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

import os, sys
sys.path.insert(0,'/home/cecyf/rails')
sys.path.insert(0,'/home/cecyf/rails/rawsaladwebsite')
sys.path.insert(0,'/home/cecyf/rails/rawsaladwebsite/site-packages')

os.environ['PYTHON_EGG_CACHE'] = '/usr/lib/django_eggs/d920_cecyf' 
os.environ['DJANGO_SETTINGS_MODULE'] = 'rawsaladwebsite.settings'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib'

import django.core.handlers.wsgi

#lapie bledy 500 ale potencjalnie wolniejsza metoda uruchomienia
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
application = ErrorMiddleware(application, debug=True)

#nie lapie bledow 500 ale szybszy
#application = django.core.handlers.wsgi.WSGIHandler()

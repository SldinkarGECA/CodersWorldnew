"""
WSGI config for codersworld project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'codersworld.settings')

application = get_wsgi_application()
# import os
# import sys

# path = os.path.expanduser('~/CodersWorldnew')
# if path not in sys.path:
#     sys.path.insert(0, path)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'codersworld.settings'
# from django.core.wsgi import get_wsgi_application
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application())

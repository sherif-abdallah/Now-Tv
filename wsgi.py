# +++++++++++ DJANGO ++++++++++++++++++
# To use your own django app use code like this:
# +++++++++++ Pythoanywhere +++++++++++
import os
import sys

path = '/home/movies2egypt/Movies-2-Egypt/'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
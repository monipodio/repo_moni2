import os

import sys


from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

from django import dj_database_url


path = '/home/monipodio/misitio'

if path not in sys.path:

    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'misitio.settings'

application = get_wsgi_application()

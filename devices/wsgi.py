import os

env = os.environ.get('DJANGO_ENV') or 'local'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(["devices.settings", env]))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

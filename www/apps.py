# in yourapp/apps.py
from django.apps import AppConfig
from django.conf import settings

class WwwAppConfig(AppConfig):
    name = 'www'
    verbose_name = ' '.join([settings.COMPANY_NAME, 'Devices'])

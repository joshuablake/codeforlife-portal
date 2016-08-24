import os
from selenium import webdriver

SELENIUM_WEBDRIVERS = {
    'default': {
        'callable': webdriver.Firefox,
        'args': (),
        'kwargs': {},
    },
    'chrome': {
        'callable': webdriver.Chrome,
        'args': (),
        'kwargs': {},
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = ['portal']
PIPELINE_ENABLED = False
ROOT_URLCONF = 'django_autoconfig.autourlconf'
STATIC_ROOT = '.tests_static/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())

import os
try:
    from selenium import webdriver
except ImportError:
    pass
else:
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

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())

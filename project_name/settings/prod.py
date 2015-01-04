"""
Django production environment settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from os import environ
import dj_database_url
from memcacheify import memcacheify
from common import  *

########## EMAIL CONFIGURATION
INSTALLED_APPS += (
    # Mandrill email app integration:
    # https://djrill.readthedocs.org/en/latest/
    'djrill',
)

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-backend
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.mandrillapp.com')

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('MANDRILL_APIKEY', '')

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('MANDRILL_USERNAME', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[{{project_name}}] '

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.7/ref/settings/#caches
CACHES = memcacheify()
########## END CACHE CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
DEFAULT_FILE_STORAGE = STATICFILES_STORAGE
COMPRESS_STORAGE = DEFAULT_FILE_STORAGE

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS += [
    'compressor.filters.cssmin.CSSMinFilter',
    ]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
    ]
########## END COMPRESSION CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/1.7/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
########## END SECRET CONFIGURATION


########## SECURE_PROXY_SSL_HEADER CONFIGURATION
# https://docs.djangoproject.com/en/1.7/ref/settings/#secure-proxy-ssl-header
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
########## END SECURE_PROXY_SSL_HEADER CONFIGURATION


########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
# Allow all host headers
ALLOWED_HOSTS = ['*']
########## END ALLOWED HOST CONFIGURATION



from .common import *
import os

from dotenv import load_dotenv
load_dotenv()

DEBUG = os.environ.get("DEBUG")
PRODUCTION = os.environ.get("PRODUCTION")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


#DEFAULT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#POSTGRESQL NB need to run 'pip install psycopg2'

##add settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }


##may need to change these settings when in production!!!
STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, "staticfiles"),
    #os.path.join(BASE_DIR, 'media'),
]

#STATIC_URL= '/static/'
#MEDIA_URL = '/media/'

#STATIC_ROOT = os.path.join(BASE_DIR,'staticfile')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
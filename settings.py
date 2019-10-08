#para produccion
#import django_heroku


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e$dab5m8oustg8booype(#to1^s@@$^c1z0i=*gdlsc74p0&gc'

# SECURITY WARNING: don't run with debug turned on in production!

#desarrollo
#DEBUG = True 

#produccion
DEBUG = False 

#produccion
DEBUG_PROPAGATE_EXCEPTIONS = True

#desarrollo
#ALLOWED_HOSTS = [] 

#produccion
ALLOWED_HOSTS = ['*'] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'aintegral.ai',
 ]


CRISPY_TEMPLATE_PACK = 'bootstrap4' 

DATE_INPUT_FORMATS = ('%d-%m-%Y','%d-%m-%Y')


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

#  la linea siguiente incluirla en MIDDLEWARE para produccion
#  'whitenoise.middleware.whitenoiseMiddleware',

ROOT_URLCONF = 'aintegral.urls'
#ROOT_URLCONF = 'ai.urls'

#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': ['aintegral/ai/templates'],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.debug',
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['aintegral/ai/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# produccion
WSGI_APPLICATION = 'aintegral.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# MySql
#DATABASES = {
#    'default': {
#        'ENGINE': 'mysql_cymysql',
#        'NAME': 'asistenciaintegral',
#        'USER': 'root',
#        'PASSWORD':'',
#        'HOST':'localhost',
#        'PORT':'',
#    }
#}

#Postgresql
#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': 'asistenciaintegral',                      
#       'USER': 'postgres',
#       'PASSWORD':'toto2004',
#       'HOST': 'localhost',
#       'PORT': '5432',
#       }
#   }


#sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# bloque para produccion
import dj_database_url

#DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')    
#        )
#}
DATABASES = {
    "default": dj_database_url.config(default='sqlite:///db.sqlite3'),
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/ #auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Chile/Continental'

USE_I18N = True

USE_L10N = True

USE_TZ = True 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(PROJECT_DIR)



# para pantalla de autenticacion 
LOGIN_REDIRECT_URL = '/auth/logged_in/'
#LOGIN_URL = ''       


STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


#desarrollo
#STATICFILES_FINDERS = [
#'django.contrib.staticfiles.finders.FileSystemFinder',
#'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#]


#desarrollo
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static")

#produccion
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

#produccion
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"aintegral/aintegral/ai/static/img/")
MEDIA_URL = '/img/'


#*********** para Heroku *******
#import dj_database_url  
db_from_env = dj_database_url.config(conn_max_age=500)  
#DATABASES['default'].update(db_from_env)

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
#STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (  
#    os.path.join(BASE_DIR, 'static'),
#)

# Produccion Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


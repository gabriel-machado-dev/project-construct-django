"""
Django settings for construct_youtube project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*geo-%2(&-z*%#c0-_3q7@7b9us$!qapzv$d39ymwgbw5n5*+q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'rolepermissions',
    'estoque'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'construct_youtube.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries': {
          'filters': 'estoque.templatetags.filters',
        }
        },
    },
]

WSGI_APPLICATION = 'construct_youtube.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

"""
STATIC FILES (CSS, JavaScript, Images)

STATIC_URL É a URL que será usada para servir arquivos estáticos.
STATICFILES_DIRS É uma lista de diretórios onde o Django procurará arquivos estáticos.
STATIC_ROOT É o diretório onde os arquivos estáticos coletados serão armazenados, para quando for fazer o deploy.

Arquivo de mídia: é um arquivo que é carregado pelo usuário, como uma imagem de perfil, um vídeo, um arquivo de áudio, etc.

MEDIA_URL É a URL que será usada para servir arquivos de mídia.
MEDIA_ROOT É o diretório onde os arquivos de mídia carregados serão armazenados.
"""

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
COMO VAMOS USAR NOSSO MODEL PARA A PAGINA DE ADMIN E NAO
A DO DJANGO PRECIMOS COLOCAR O SEGUINTE COMANDO:

NOME DO APP.CLASSE
"""

AUTH_USER_MODEL = 'usuarios.Users'

ROLEPERMISSIONS_MODULE = 'construct_youtube.roles' # diretório pai + arquivo roles

# Configuração de mensagens

MESSAGE_TAGS = {
    messages.ERROR: 'alert-danger',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.INFO: 'alert-info',
    messages.DEBUG: 'alert-primary',
}
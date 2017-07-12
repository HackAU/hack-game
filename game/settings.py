import os
from django.utils import timezone
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ab6s@xb50l5w89l8q%qn9ou3&(3tf9)h*fwbuu%i&bm=3tyj@o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'hack-game-test.herokuapp.com',
    'localhost'
]


INSTALLED_APPS = [
    'gameapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


# Application definition
AUTH_USER_MODEL = 'gameapp.User'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'game.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'game.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_the_game',
#         'USER': 'postgres',
#         'PASSWORD': '9352221'
#     }
# }

DATABASES = {}
DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Challenges and Event config

EVENT_START = timezone.datetime(
    2017, 7, 11, 0, 0, tzinfo=timezone.pytz.timezone('CET'))
EVENT_DURATION = timezone.timedelta(days=1)

# Array with tuples, containing the html file, and its password
LEVEL_INFO = [
    ('simple_sum.html', ['1379']),
    ('offset.html', ['1337']),
    ('captain_sonar.html',  ['501510']),
    ('balanced_palindromes.html', ['1']),
    ('puzzle.html',  ['hackupcrules']),
    ('editor.html',  ['vimisbetterthanemacs']),
    ('going_home.html', ['1147372005']),
    ('hidden_message.html',  ['isitnergunbattletime']),
    ('custom_id.html',  ['99379127581167914']),
    ('broken_document.html', [
        '1223512201493211017079467541693136328292324432464582475861864920694407578768023144072628540276213813397768975366156750120']),
    ('private_lessons.html',  ['3250940697']),
    ('box_management.html',  ['10876472606873674']),
]

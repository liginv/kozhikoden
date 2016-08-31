import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gn1l^b__&+a3mute%fkbdm4t5mrb4-@5zl6r51xe^)7g_l2yi8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'tastypie',
    'geoposition',
    'rest_framework',
    # 'imagekit',
    # djangorestframework==3.3.3
]

PROJECT_APPS = [
    'movies',
    'restaurents',
    'culturals',
    'events',
    'homepage',
]
INSTALLED_APPS = CORE_APPS + PROJECT_APPS + THIRD_PARTY_APPS

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

ROOT_URLCONF = 'kozhikoden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'loader': [
            #   'django.template.loaders.filesystem.Loader',
            #   'django.template.loaders.app_directories.Loader',
            #   ],
        },
    },
]

WSGI_APPLICATION = 'kozhikoden.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, 'static'),
                    )

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'

GEOPOSITION_GOOGLE_MAPS_API_KEY = ' AIzaSyDxd538__HtXgMiIpTohSMaYMxE-S4XWFw '

# Update database configuration with $DATABASE_URL.
STATICFILES_DIRS = (
       # put absolute path here as string not relative path.
       # forward slash to be used even in windows.
       os.path.join(
                    os.path.dirname(__file__),
                    'static',
                    ),
       )

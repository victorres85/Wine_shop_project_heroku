from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+%)59bb-wx7*0j9625oa&zs8(!&gh2xv+rplfm_uzlhh6sw*aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0', '127.0.0.1', 'localhost', 'wine-shop-project.herokuapp.com/',
    'wine-shop-project.herokuapp.com'
]

CSRF_TRUSTED_ORIGINS = ["https://wine-shop-project.herokuapp.com"]

# a
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'payment.apps.PaymentConfig',
    'orders.apps.OrdersConfig',
    'django_celery_beat',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'wine_shop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'wine_shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd533kovdp1rulp',
        'USER': 'jkpsdgqzygnvmr',
        'PASSWORD':
        'bf480b48251a7e0fed82c9e868d5fe5c5ba4bce3c8798a491058620e45b6c26c',
        'HOST': 'ec2-52-30-75-37.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticFiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

CART_SESSION_ID = 'cart'

# STRIP SETTINGS
STRIPE_PUBLISHABLE_KEY = 'pk_test_51LTsEwAnyQlDbgoYzQdEvp3Xg9zqWSS5rtiEcMqcNpUXikA648ZzNfsWcci2P3fSxLEe2uRPSLdFKxSFSUCMlqP800TGxujuYs'  # PUBLISHABLE KEY
STRIPE_SECRET_KEY = 'sk_test_51LTsEwAnyQlDbgoYrb5fGxl4xxG9LfZRiiIoSgtg5RiUllK0hn4AZExZxzdxg8fsgT4r3Ne8sdCm3HKUzsA7uyzq00Yk97Zlan'  #SECRET KEY

STRIPE_WEBHOOK_SECRET = 'whsec_9add87442f529215da2f5b778f7b3f497cef37002b0811b1c1221dc916eea42f'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#  Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'victorres.emailtest@gmail.com'
EMAIL_HOST_PASSWORD = 'vwriiyfdaixevizz'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
 # CELERY_RESULT_BACKEND = "django-db"
# This configures Redis as the datastore between Django + Celery
CELERY_BROKER_URL = config('CELERY_BROKER_REDIS_URL', default='redis://paf878bdf156761e7d20ea352865d643c02bac79da28fce83c716a73e7e762054@ec2-52-210-234-212.eu-west-1.compute.amazonaws.com:9610')

# REDIS_PASSWORD ='paf878bdf156761e7d20ea352865d643c02bac79da28fce83c716a73e7e762054'


# this allows you to schedule items in the Django admin.

#CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

#CELERY_BROKER_URL = f'redis://localhost:6379/4'
#CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
#CELERY_RESULT_BACKEND = f'redis://localhost:6379/1'


#----HEROKU----
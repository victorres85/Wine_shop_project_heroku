from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+%)59bb-wx7*0j9625oa&zs8(!&gh2xv+rplfm_uzlhh6sw*aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','https://wine-shop-project.herokuapp.com/', 'wine-shop-project.herokuapp.com']


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
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME',''),
        'USER': os.environ.get('DB_USER',''),
        'PASSWORD': os.environ.get('DB_PASSWORD',''),
        'PORT': 5432,
    }
}



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticFiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

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
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")


#  Email server configuration
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")
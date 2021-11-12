"""
Django settings for Eggoz project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import environ
import pytz
from celery.schedules import crontab
from django.utils.timezone import get_current_timezone

from Eggoz import dev_settings
from Eggoz import local_settings
from Eggoz import prod_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(DEBUG=(bool, True))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'n8x&)#(o74@_umh6$w5_9zr!klq$=+5lgey2ak4#85z^#jhc5+'

SECRET_KEY = open(os.path.join(BASE_DIR, 'secret_key.txt')).read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PROD_STATUS = env('PROD_STATUS', default=False)
# EGGOZ_ENV = env('EGGOZ_ENV', default="local")
PHONE_SMS_ON = env('PHONE_SMS_ON', default=False)

# PROD_STATUS = True
# DEBUG = False

EGGOZ_ENV = "local"
ALLOWED_HOSTS = ['*']

# Application definition


DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS = ['phonenumber_field',
                    'django_countries',
                    'django_extensions',
                    'prices',
                    'draftjs_sanitizer',
                    'corsheaders',
                    'rest_framework',
                    'django_prices',
                    'nested_admin',
                    'drf_yasg', 'django_celery_beat', 'django_celery_results']

LOCAL_APPS = ['base.apps.BaseConfig',
              'custom_auth.apps.AuthConfig',
              'order.apps.OrderConfig',
              'product.apps.ProductConfig',
              'payment.apps.PaymentConfig',
              'retailer.apps.RetailerConfig',
              'saleschain.apps.SaleschainConfig',
              'supplychain.apps.SupplychainConfig',
              'operationschain.apps.OperationschainConfig',
              'warehouse.apps.WarehouseConfig',
              'feedback.apps.FeedbackConfig',
              'farmer.apps.FarmerConfig',
              'feedwarehouse.apps.FeedwarehouseConfig',
              'mqtt.apps.MqttConfig',
              'ecommerce.apps.EcommerceConfig',
              'distributionchain.apps.DistributionchainConfig',
              'finance.apps.FinanceConfig',
              'procurement.apps.ProcurementConfig',
              ]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'Eggoz.utils.my_jwt_response_handler',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300000),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_ALLOW_REFRESH': True,
}

if PROD_STATUS:
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 1000,
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'EXCEPTION_HANDLER': 'base.exceptions.exception_handler',
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 1000,
        # 'DEFAULT_PERMISSION_CLASSES': (
        #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'EXCEPTION_HANDLER': 'base.exceptions.exception_handler',
    }

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost',
    'http://127.0.0.1:5500',
    'http://stage.eggoz.in:8000',
    'http://stage.eggoz.in',
    'https://eggoz.in',
    'https://www.eggoz.in',
    'http://localhost:4000',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'Eggoz.urls'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'phone_number'
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
        },
    },
]

WSGI_APPLICATION = 'Eggoz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


if EGGOZ_ENV == "PROD":
    DATABASES = prod_settings.DATABASES
    PHONE_SMS_ON = True
elif EGGOZ_ENV == "DEV":
    DATABASES = dev_settings.DATABASES
    PHONE_SMS_ON = False
else:
    DATABASES = local_settings.DATABASES
    PHONE_SMS_ON = False

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'custom_auth.User'

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

# USE_TZ = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

# try:
#     from .local_settings import *
# except ImportError:
#     pass


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "info@eggoz.in"
EMAIL_HOST_PASSWORD = "eggoz@123"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_MAX_DIGITS = 12
DEFAULT_DECIMAL_PLACES = 3
DEFAULT_CURRENCY_CODE_LENGTH = 3
DEFAULT_CURRENCY = 'INR'

SESSION_EXPIRY = 18000

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGIN_REDIRECT_URL = "/sales"

LOGOUT_REDIRECT_URL = "/signin"

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default="redis://localhost:6379")
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default="redis://localhost:6379")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = env('CELERY_TIMEZONE', default=TIME_ZONE)  # Use django's timezone by default

WEATHER_API = env("WEATHER_API", default="")

if EGGOZ_ENV == "PROD":
    CELERY_BEAT_SCHEDULE = {
        'sales_daily_report': {
            'task': 'saleschain.tasks.sales_daily_report',
            'schedule': crontab('0', '7', '*', '*', '*')
        }
    }
IST = pytz.timezone(TIME_ZONE)
CURRENT_ZONE = get_current_timezone()

# Payment Gateway
CASHFREE_BASE_URL = env('CASHFREE_BASE_URL', default="https://test.cashfree.com")
CASHFREE_APP_ID = env('CASHFREE_APP_ID', default="70107d28fba5bb0df3eae8a3770107")
CASHFREE_SECRET_KEY = env('CASHFREE_SECRET_KEY', default="2ee0f992df29a97d2af083490953353c60bf4265")
if EGGOZ_ENV == "PROD":
    PAYMENT_SUCCESS_REDIRECT_URL = env('PAYMENT_SUCCESS_REDIRECT_URL', default="https://eggoz.in/paymentSuccess")
    PAYMENT_SUCCESS_REDIRECT_WALLET_URL = env('PAYMENT_SUCCESS_REDIRECT_WALLET_URL',
                                              default="https://eggoz.in/paymentSuccess/?status=PaidByWallet")
    PAYMENT_SUCCESS_REDIRECT_CARD_URL = env('PAYMENT_SUCCESS_REDIRECT_CARD_URL',
                                            default="https://eggoz.in/paymentSuccess/?status=Paid")
    PAYMENT_FAILED_REDIRECT_URL = env('PAYMENT_FAILED_REDIRECT_URL', default="https://eggoz.in/paymentFailed")
    PAYMENT_FAILED_REDIRECT_UNPAID_URL = env('PAYMENT_FAILED_REDIRECT_UNPAID_URL',
                                             default="https://eggoz.in/paymentFailed/?status=UnPaid")
    PAYMENT_FAILED_REDIRECT_FAIL_URL = env('PAYMENT_FAILED_REDIRECT_FAIL_URL',
                                           default="https://eggoz.in/paymentFailed/?status=Fail")
else:
    PAYMENT_SUCCESS_REDIRECT_URL = env('PAYMENT_SUCCESS_REDIRECT_URL', default="https://stage.eggoz.in/paymentSuccess")
    PAYMENT_SUCCESS_REDIRECT_WALLET_URL = env('PAYMENT_SUCCESS_REDIRECT_WALLET_URL',
                                              default="https://stage.eggoz.in/paymentSuccess/?status=PaidByWallet")
    PAYMENT_SUCCESS_REDIRECT_CARD_URL = env('PAYMENT_SUCCESS_REDIRECT_CARD_URL',
                                            default="https://stage.eggoz.in/paymentSuccess/?status=Paid")
    PAYMENT_FAILED_REDIRECT_URL = env('PAYMENT_FAILED_REDIRECT_URL', default="https://stage.eggoz.in/paymentFailed")
    PAYMENT_FAILED_REDIRECT_UNPAID_URL = env('PAYMENT_FAILED_REDIRECT_UNPAID_URL',
                                             default="https://stage.eggoz.in/paymentFailed/?status=UnPaid")
    PAYMENT_FAILED_REDIRECT_FAIL_URL = env('PAYMENT_FAILED_REDIRECT_FAIL_URL',
                                           default="https://stage.eggoz.in/paymentFailed/?status=Fail")


FCM_SERVER_KEY = "AAAAKkGUPa8:APA91bGftLMLOD_b0K_Q852tLL3J4edgS0QYroD4aU9NvwpUkKq3JOn_vdZtcwDgzDrOl9g0CwqCkk75ZBMgAngI10XCTQy75Ivk1WumI3NveGHcpdJe-z299k32c5XHcxiL_UXcYXUT"
IOT_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijh2OFp2alN2MWY2UWg3V1hvNG9qZSJ9"

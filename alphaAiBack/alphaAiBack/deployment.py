import os

from .settings import *
from .settings import BASE_DIR
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework',
    'user',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  
# ]


STORAGES = {
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage"
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Get the connection string from the environment variable
CONNECTION_STR = os.environ.get('AZURE_SQL_CONNECTIONSTRING')

# Validate if the connection string exists
if not CONNECTION_STR:
    raise ValueError("AZURE_SQL_CONNECTIONSTRING is not set in environment variables.")



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AlphaAi',
        'USER': 'rgdtfwming',
        'PASSWORD': '$0BuDlj$Yf5IlByq',
        'HOST':'alpha-ai-dashboard-server.postgres.database.azure.com',
        'PORT':'5432',
    }
}


print("===================2223333333334444444", DATABASES)

STATIC_ROOT = BASE_DIR/'staticfiles'

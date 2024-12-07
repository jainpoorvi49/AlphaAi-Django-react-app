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

# Parse the connection string
# connection_dict = {}
# for part in CONNECTION_STR.split(';'):
#     if '=' in part:
#         key, value = part.split('=', 1)
#         connection_dict[key.strip()] = value.strip()

# # Extract HOST and PORT from the connection string
# host_port_part = CONNECTION_STR.split('://')[-1].split(';')[0]
# host, port = host_port_part.split(':') if ':' in host_port_part else (host_port_part, '1433')

# print("==================host",host)
# print("================>>>>>>>>>", host_port_part)

# # Database configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': connection_dict.get('database'),
#         'HOST': host,
#         'PORT': port,
#         'USER': connection_dict.get('user'),
#         'PASSWORD': connection_dict.get('password'),
#         'OPTIONS': {
#             'driver': 'ODBC Driver 18 for SQL Server',
#             'encrypt': 'no',
#             'trustServerCertificate': 'yes',
#             'timeout': 60,
#         },
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'alphaai',  # Your database name
#         'USER': 'alphaadmin',  # Your database username
#         'PASSWORD': 'Alphaaifund@123',  # Your password
#         'HOST': 'alphaaisql.database.windows.net',  # Your SQL Server host
#         'PORT': '1433',  # Default port for SQL Server
#         'OPTIONS': {
#             'driver': 'ODBC Driver 18 for SQL Server',  # ODBC driver for SQL Server
#             'encrypt': 'yes',  # Encrypt the connection
#             'trustServerCertificate': 'no',  # Don't trust server certificate, use proper SSL certificates
#             'Connection Timeout': 30,  # Connection timeout in seconds
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AlphaAi',
        'USER': 'root',
        'PASSWORD': 'Jain@123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


print("===================2223333333334444444", DATABASES)

STATIC_ROOT = BASE_DIR/'staticfiles'

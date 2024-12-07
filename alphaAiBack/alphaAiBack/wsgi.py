"""
WSGI config for alphaAiBack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from django.core.wsgi import get_wsgi_application
# settings_module = 'alphaAiBack.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'alphaAiBack.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alphaAiBack.settings')

application = get_wsgi_application()

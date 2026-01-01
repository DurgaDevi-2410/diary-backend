import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

print("DATABASE SETTINGS:")
print(settings.DATABASES['default'])

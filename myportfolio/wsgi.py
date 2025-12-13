"""
WSGI config for myportfolio project.
"""

import os
import sys
from environ import Env
from django.core.wsgi import get_wsgi_application

# Load environment variables
env = Env()
env.read_env()

# Add project path (important for PythonAnywhere)
project_path = "/home/sagarnanera/myportfolio"
if project_path not in sys.path:
    sys.path.append(project_path)

# Force production settings
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "myportfolio.settings.production"
)

application = get_wsgi_application()

"""
WSGI config for TweetUs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TweetUs.settings')

application = get_wsgi_application()

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 4000))
  get_wsgi_application.run(host ="0.0.0.0", port=port)

import os

CELERY_BROKER_URL = os.environ.get('BROKER_URL', 'redis://redis:6379'),
CELERY_RESULT_BACKEND = os.environ.get('RESULT_BACKEND', 'redis://redis:6379')
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'postiks.settings')

BASE_REDIS_URL = os.environ.get('REDIS_URL')

app = Celery('postiks')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


app.conf.beat_schedule = {
    'clear_upvotes_every_day': {
        'task': 'clear_upvotes',
        'schedule': crontab(minute=0, hour=0),
    },
}

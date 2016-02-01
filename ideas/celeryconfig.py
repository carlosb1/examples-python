from celery.schedules import crontab
from datetime import timedelta

CELERY_BROKER_URL="amqp://guest@localhost//"
CELERYBEAT_SCHEDULE = {
	'every-day': {
		'task': 'forecast.search_spot',
		'schedule': timedelta(seconds=10),
	}
}
CELERY_TIMEZONE='UTC'

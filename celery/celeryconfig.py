from datetime import timedelta
BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'US/Eastern'
#CELERY_ENABLE_UTC = True

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=5),
        'args': (16, 16)
    },
}

CELERY_ROUTES = {'tasks.add' : {'queue':'celery'}}

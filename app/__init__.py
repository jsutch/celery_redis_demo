from celery import Celery
 
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
 
def create_app(config_name):
    app = Flask(__name__)
    
    celery.conf.update(app.config)

class Config:
    CELERYBEAT_SCHEDULE = celery_get_manifest_schedule
    # Development setup:
    if not is_prod:
        CELERY_BROKER_URL = 'redis://server2:6379/0'
        CELERY_RESULT_BACKEND = 'redis://server2:6379/0'
        REDIS_HOST = 'server2'
        REDIS_PASSWORD = 'notARealPassword'
        REDIS_PORT = 6379
        REDIS_URL = 'redis://server2:6379/0'

    # Production setup:
    else:
        # Celery:
        CELERY_BROKER_URL = os.environ.get('REDIS_URL')
        CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL')
        # Redis:
        REDIS_URL = os.environ.get('REDIS_URL')

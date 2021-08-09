#定义消息中间件和数据库
from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379/15'
#CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/14'
CELERY_RESULT_BACKEND= 'django-db'

#  每个worker最多执行3个任务就会被销毁，可防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 3

CELERY_RESULT_SERIALIZER = 'json'  # 结果序列化方案

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# CELERYBEAT_SCHEDULE = {
#      # 名字随意命名
#      'add-every-10-seconds': {
#          # 执行tasks1下的test_celery函数
#          'task': 'mycelery.cms2.tasks.chains_check',
#          # 每隔2秒执行一次
#          # 'schedule': 2.0,
#          #每1分钟执行一次
#          # 'schedule': crontab(minute="*/1"),
#          'schedule': timedelta(seconds=10),
#          # 传递参数
#          #'args': ('张三',)
#      },
#  }
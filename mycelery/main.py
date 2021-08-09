# 主程序
import os
# import django
# django.setup()


from celery import Celery
# 创建celery实例对象
from ZxWebTest import settings

app = Celery("sms")


# 把celery和django进行组合，识别和加载django的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZxWebTest.settings')

import django

django.setup()


# 通过app对象加载配置
app.config_from_object("mycelery.config")
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.sms","mycelery.cms2"])

# 启动Celery的命令
# 强烈建议切换目录到mycelery根目录下启动
# celery -A mycelery.main worker --loglevel=info
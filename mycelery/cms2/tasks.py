# celery的任务必须写在tasks.py的文件中，别的文件名称不识别!!!
from mycelery.main import app
import time
import logging
log = logging.getLogger("django")



@app.task  # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
def chains_check():

    print("开始执行链路检查!")
    time.sleep(5)

    return "检查完毕"

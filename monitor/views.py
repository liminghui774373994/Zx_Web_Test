from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from pymysql import connect
from sshtunnel import SSHTunnelForwarder
from pymysql import connect
from sshtunnel import SSHTunnelForwarder
#from monitor.tasks import add
from ZxWebTest import settings
from mycelery.sms.tasks import send_sms,send_sms2
from mycelery.cms2.tasks import chains_check
from datetime import timedelta
from datetime import datetime
#from django_celery_beat.models import PeriodicTask  #倒入插件model




def view(request):
    """生产者"""
    ################################# 异步任务

    # 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决
    #chains_check.delay()
    #send_sms.delay("110")
    send_sms2.delay("119")
    #send_sms.delay() #如果调用的任务函数没有参数，则不需要填写任何内容
    print('-------------')
    return JsonResponse({"status": 0})



#
# def crontab(request):
#
#     ################################ 定时任务
#
#     ctime = datetime.now()
#     # 默认用utc时间
#     utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
#     time_delay = timedelta(seconds=10)
#     task_time = utc_ctime + time_delay
#     result = send_sms.apply_async(["911", ], eta=task_time)
#     print(result.id)
#     return JsonResponse({"status": 'ok'})

#
# def cms2_task_list(request):
#     #page = request.GET.get('page');
#     # if page:
#     #     page=int(page);
#     # else:
#     #     page=1;
#
#     tasks = PeriodicTask.objects.all()
#     print(tasks)
#     # paginator = Paginator(tasks, settings.PAGE_SIZE)
#     # task_list = []
#     return JsonResponse({"data":tasks})







def db_content(sql_sentence):
    server = SSHTunnelForwarder(
        ssh_address_or_host=('xxx', 22),  # 指定SSH中间登录地址和端口号
        ssh_username='root',  # 指定地址B的SSH登录用户名
        ssh_password='xxx',  # 指定地址B的SSH登录密码
        remote_bind_address=('xxxx', 3306)  # 指定最终目标C地址，端口号为mysql默认端口号3306
    )
    server.start()

    db = connect(
        host='127.0.0.1',  # 此处必须是是127.0.0.1
        port=server.local_bind_port,
        user='xxx',
        passwd='xxxx',
        db='xxx')
    print("端口：" + str(server.local_bind_port))

    cursor = db.cursor()
    # print(cursor)

    db.ping(reconnect=True)
    cursor.execute(sql_sentence)
    results = cursor.fetchall()
    # print(results)
    server.close()
    return results


def chains(request):
    results = db_content('xxx')
    if results:
        print('fail')
        list1 = list(results)
        list_result = []
        for i in list1:
             a = i.__str__().replace(',', '').strip('()')
             list_result.append(a)
        print(list_result)
        return JsonResponse({"status": 0, "message": list_result})
    else:
        return JsonResponse({"status": 0, "message": '无异常！'})







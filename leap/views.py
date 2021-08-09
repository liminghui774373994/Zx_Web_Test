from django.shortcuts import render

# Create your views here.

#views部分代码

from django.http import HttpResponse, JsonResponse
import json

import hmac
import hashlib
import base64
from common.db import Mysql
from common.geturl import ApiRequest
import time
import calendar


# 机器人的app_secret
app_secret = "qDAmlsyG0yrZZOSoM3vk4gWKtrX0zhYG8cU7QOL1LOx6agQB0wPSSboRtFnIArlE"

# Create your views here.
def robot(request):
    if request.method == "POST":
        HTTP_SIGN = request.META.get("HTTP_SIGN")
        HTTP_TIMESTAMP = request.META.get("HTTP_TIMESTAMP")
        res = json.loads(request.body)
        print(res)
        # 用户输入钉钉的信息
        content = res.get("text").get("content")
        print(content)
        string_to_sign = '{}\n{}'.format(HTTP_TIMESTAMP, app_secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(app_secret.encode("utf-8"), string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = base64.b64encode(hmac_code).decode("utf-8")
        print(sign)
        print(HTTP_SIGN)
        #验证签名是否为钉钉服务器发来的
        if sign == HTTP_SIGN:
            '''
            可以写一些执行逻辑，返回用户想要的信息
            '''
            if "我的工作" in content:
                return JsonResponse(
                    {"msgtype": "text",
                     "text": {
                         "content": "您是一名测试！"
                     }
                     }
                )
            return JsonResponse(
                {"msgtype": "text",
                 "text": {
                     "content": "谢谢使用此机器人，{}".format(content)
                 }
                 }
            )
        return JsonResponse({"error":"你没有权限访问此接口"})
    if request.method == "GET":
        return HttpResponse("hello")


def creat_class(request,is_uplode=0):
    subject = str(request.GET.get('subject'));
    add_student = Mysql()
    created_at = str(calendar.timegm(time.gmtime()))
    updated_at = str(calendar.timegm(time.gmtime()))
    add_student.insert_sql("xxx")

    class_id = add_student.select_sql(
        "SELECT xx FROM xx WHERE created_at=" + created_at + " AND updated_at=" + updated_at + ";")
    print("建班成功，class_id=" + str(class_id))

    if is_uplode !=0:
        print('上传课表')
    else:
        print('清除缓存')

    return HttpResponse(class_id,content_type='application/json', charset='utf-8')

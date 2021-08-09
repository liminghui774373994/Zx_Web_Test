import json
import os
from django.shortcuts import render
from django.http import HttpResponse, response, FileResponse
from django.http import JsonResponse
# Create your views here.
from django.utils.encoding import escape_uri_path
from numpy.distutils.conv_template import header
from ZxWebTest import settings
from myxmind.models import Xmind_file
from myxmind.xmind_toExcel import xmind_to_xls
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User  # django封装好的验证功能
from django.contrib import auth


def post(request):
    try:
        data = json.loads(request.body)
        user = data.get("username")
        pwd = data.get("password")
        print(user)
        # 验证密码
        obj = auth.authenticate(request, username=user, password=pwd)
        if obj:
            return JsonResponse({'code': 0, 'message': '账号密码验证成功'})
        else:
            return JsonResponse({'code': 1, 'message': '账号密码验证失败'})
    except:
        return JsonResponse({'code': 2, 'message': '参数错误'})


def test(request):

    return JsonResponse({"status":0,"message":"This is django message new"})
    #return HttpResponse('xmind路径哈哈哈哈')



def file_down(request):
    file_path = '{}/download/{}'.format(settings.MEDIA_ROOT, 'excel_data.xls')
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename*=utf-8;filename="BatchPayTemplate.xls"'
    return response



def exchange(request):
    print(request.body)
    try:
        data = json.loads(request.body)
        xmind_file = data.get("xmind_file_path")
        print(xmind_file)
        xmind_to_xls().write_excel(xmind_file)
        # 验证密码
        return JsonResponse({"status":0,"message":"转换成功！"})
    except:
        return JsonResponse({'code': 10002, 'message': '参数错误'})



def upload(request):
    print(request.body)
    image = request.FILES.get('image', None)
    print(image)
    image_name = image.name
    #print(image.chunks) # 获取文件内容
    save_path = '{}/upload/{}'.format(settings.MEDIA_ROOT, 'xmind_data.xmind')
    with open(save_path, 'wb') as f:
        for content in image.chunks():
            f.write(content)
    # 报存到数据库
    #FileUpload.objects.create(name=img.name)
    return JsonResponse({"status": 0, "message": save_path})

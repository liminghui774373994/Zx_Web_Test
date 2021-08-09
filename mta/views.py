import json

from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from ZxWebTest import settings
from mta import models
from mta.excel_data import Data_excel
from mta.models import Event
from mta.sensors_data import Data_sensors


def mta_add(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        event_name = req.get("event_name")
        # 判断请求体是否正确
        if event_name:
            event_name = req.get('event_name', 'event')
            event_en = req.get('event_en', 'event_en')
            attribute_en = req.get('attribute_en', 'attribute_en')
            event_sh = req.get('event_sh', 'event_sh')
            type = req.get('type','type')
            description = req.get('description', 'description')
            data = request.POST.get('data', '2020')

            '''插入数据'''
            #add_ene = Event(event_name=event_name)
            add_ene = Event(event_name=event_name, event_en=event_en, attribute_en=attribute_en,event_sh=event_sh, type=type, description=description, data=data)
            add_ene.save()
            return JsonResponse({"status": 0, "message": "publish event sucess."})
        else:
            return JsonResponse({"status": 400, "message": "please check param."})


def mta_list(request):
    page = request.GET.get('page');
    if page:
        page = int(page);
    else:
        page = 1;

    mtas = Event.objects.all()
    paginator = Paginator(mtas, settings.PAGE_SIZE)
    mtas_page_list = paginator.page(page);
    mta_list = []
    for mta in mtas_page_list:
        json_dict = {}
        # 获取埋点的属性字段
        json_dict['id'] = mta.id
        json_dict['event_name'] = mta.event_name
        json_dict['event_en'] = mta.event_en
        json_dict['attribute_en'] = mta.attribute_en
        json_dict['event_sh'] = mta.event_sh
        json_dict['type'] = mta.type
        json_dict['description'] = mta.description
        mta_list.append(json_dict)

    print(mta_list)
    # 用json.dumps(json_list)将json_list进行序列化
    #return HttpResponse(json.dumps(mta_list),content_type='application/json')
    return JsonResponse({"status": 0, "message": mta_list})


def check_data(request):
    print(request.body)
    try:
        data = json.loads(request.body)
        excel_file = data.get("Excel_file")
        print(excel_file)
        Data_diff(excel_file).find_parmas_error()
        # 验证密码
        return JsonResponse({"status":0,"message":"转换成功！"})
    except:
        return JsonResponse({'code': 10002, 'message': '参数错误'})


class Data_diff():
    '''data1是需求数据'''
    a = Data_excel()
    data1=a.get_true_data()
    #print(data1)

    '''data2是神策数据'''
    b = Data_sensors()
    data2=b.get_sensors_data()

    '''data3是需求事件,需要去重'''
    data3=a.get_excel_event()
    data33 = {}.fromkeys(data3).keys()
    list1=list(data33)

    '''data4是神策事件'''
    list2=b.get_sensors_event()
    comm = set(list1).intersection(set(list2))
    listcomm = list(comm)


    def find_event_lose(self):
        # 漏报，在list1中没有在list2中;list1-listcomm
        event_lose = []
        for i in self.list1:
            if i not in self.listcomm:
                event_lose.append(i)
            else:
                pass
        return event_lose

    def find_event_duplication(self):
        event_duplication_1 = []
        for j in self.list2:
            if self.list2.count(j) > 1 and j in self.listcomm:
                event_duplication_1.append(j)
        event_duplication = list(set(self.list2))
        return event_duplication



    def  find_parmas_error(self):
        # 检查已上报的属性与神策属性是否一致
        '''获取参数不一致的事件属性'''
        diff = self.data1.keys() & self.data2
        '''获取参数不一致的参数，已经去掉Excel中参数为空的数据'''
        diff_vals = [(k, self.data1[k], self.data2[k]) for k in diff if self.data1[k] != self.data2[k] and self.data1[k] != ['{}']]
        print(diff_vals)
        return diff_vals



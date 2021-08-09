"""
author：liminghui
time：2020-10-29
description：''
"""
import json
import requests



class ApiRequest(object):
    cookies = 'PHPSESSID=d6dfaf2e256749184e4fbdf3f9004a2f'
    header = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Connection': 'close',
              'cookie': cookies, }

    def get_method(self,url,data=None):
        res=requests.get(url,params=data,headers=self.header, verify=False)
        return res.json()



    def post_method(self,url,data=None):
        global res
        res=requests.post(url,data=data,headers=self.header, verify=False)


        return res.text


    # 请求方法put
    def put_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.put(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()

    # 请求方法delete
    def delete_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.delete(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()




    def run_method(self,method,url,data=None):
        if method== 'get' or method=='GET':
            res=self.get_method(url,data)
        elif method == 'post' or method == 'POST':
            res = self.post_method(url, data)
        elif method == 'put' or method == 'PUT':
            res = self.post_method(url, data)
        elif method == 'delete' or method == 'DELETE':
            res = self.post_method(url, data)
        else:
            res = "你的请求方式不正确！"

        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True,separators=(',', ':'))



from xmindparser import xmind_to_dict
import re
import xlwt

from ZxWebTest import settings


class xmind_to_xls():
    def __init__(self):
        self.workbook = None

    def xmind_num(self,value):
        """获取xmind标题个数"""
        try:
            return len(value['topics'])
        except KeyError:
            return 0

    def xmind_title(self,value):
        """获取xmind标题内容"""
        return value['title']

    def  xmind_cat(self,filename):
        '''调试函数，打印内容用的'''
        self.out = xmind_to_dict(filename)
        self.story = self.out[0]['topic']['topics']
        self.num=len(self.story)
        print(self.out)
        print(self.out[0]['topic']['title'])
        return self.story,self.num



    def write_excel(self,xmind_file):
        '''生成excel文件函数'''
        self.f=xlwt.Workbook(encoding = 'utf-8')
        self.sheet1 =self.f.add_sheet('sheet1',cell_overwrite_ok=True)
        self.row0 = ["所属模块", '用例标题', '前置条件', '步骤', '预期','优先级','用例类型']
        #生成第一行
        for i in range(0,len(self.row0)):
            self.sheet1.write(0,i,self.row0[i])
        self.out = xmind_to_dict(xmind_file)
        '''画布一级节点名称'''
        self.xls_name=self.out[0]['topic']['title']
        '''全部用例集'''
        #print(self.xls_name)---链路管理
        self.story = self.out[0]['topic']['topics']
        print(self.story)
        '''计算有多少用例集'''
        self.storynum = len(self.story)
        #print(self.storynum)--2
        j=1 #用例计算器
        z = 0  # 用例结果数计数器
        for i in range(0, self.storynum):
             '''获取用例集名称'''
             self.storyname = self.story[i]['title']
             #print(self.storyname)
             self.regex_str = ".*[\[【](.+?)[\]】].*"
             self.storyid_reg = re.match(self.regex_str, self.storyname)
             if self.storyid_reg:
                 self.storyid=self.storyid_reg.group(1)#正则取出用例编号
             '''第一个用例集下面用例标题数量'''
             self.testcase_num = len(self.story[i]['topics'])
             for k in range(0,self.testcase_num):
                   '''获取一个用例标题下面的全部信息'''
                   self.testcase=self.story[i]['topics'][k]
                   '''获取用例标题名称'''
                   self.testcase_name=self.testcase['title']
                   #print(self.testcase)
                   #print(self.testcase_name)
                   '''获取用例步骤个数'''
                   self.testcase_stepnum = len(self.testcase['topics'])
                   #写入
                   self.sheet1.write(k + i + z + j, 0, self.storyname)
                   self.sheet1.write(k + i + z + j, 1, self.testcase_name)
                   '''步骤预期数据'''
                   self.case = self.testcase['topics']
                   #print(self.case)
                   self.list1 = [j['title'] for j in self.case]
                   self.list1_key = []
                   for index in range(1, len(self.list1) + 1):
                       self.list1_key.append(index)
                   self.case_title = str(dict(zip(self.list1_key,self.list1))).strip('{,}').replace("'",'')
                   self.sheet1.write(k + i + z + j, 3,self.case_title.replace(',','\n').replace(': ','.'))
                   for x in self.case:
                       print(x.get('topics'))

                   '''预期结果数据'''
                   self.a = [x.get('topics') for x in self.case]
                   self.list2 = [j[0].get('title') for j in self.a]
                   print(self.list2)
                   self.case_result = str(dict(zip(self.list1_key,self.list2))).strip('{,}').replace("'",'')
                   self.sheet1.write(k + i + z + j, 4, self.case_result.replace(',','\n').replace(': ','.'))
                   '''默认用例类型为功能测试'''
                   self.sheet1.write(k + i + z + j, 6, '功能测试')
                   '''获取用例优先级暂不支持'''
                   # '''步骤拆分'''
                   # for x in range(0,self.testcase_stepnum):
                   #     '''获取用例步骤'''
                   #     self.testcase_title=self.testcase['topics'][x]['title']
                   #     #print(self.testcase_title)
                   #     '''获取预期结果'''
                   #     self.testcase_step = self.testcase['topics'][x]
                   #     self.testcase_result = self.testcase_step.get('topics')
                   #     #print(self.testcase_result)
             j=j+k

        save_path = '{}/download/{}'.format(settings.MEDIA_ROOT, 'excel_data.xls')
        self.f.save(save_path) #xls名称取xmind主题名称


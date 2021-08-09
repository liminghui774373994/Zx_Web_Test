import os
import allure
import pytest
from data_diff import Data_diff


@allure.feature("埋点事件上报")
class Test_Checkdata:
    #对比出未上报的事件
    event = Data_diff()
    data1 = event.find_event_lose()
    #获取pytest数据参数
    data2 = []
    for i in range(len(data1)):
        data2.append('-检查event未上报')
    data_tulpe = list(zip(data1, data2))
    #print(data_tulpe)

    @allure.story('事件埋点漏报')
    @pytest.mark.parametrize('event,expectedalert',data_tulpe)
    def test_1(self, event, expectedalert):
        assert event == expectedalert


    data3 = event.find_event_duplication()
    data4 = []
    for j in range(len(data3)):
        data4.append("-检查event重复上报")
    data_dup = list(zip(data3,data4))
    #print(data_dup)
    @allure.story('事件埋点重复上报')
    @pytest.mark.parametrize('event,expectedalert', data_dup)
    def test_2(self, event, expectedalert):
        assert event == expectedalert








# if __name__ =="__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
#     pytest.main(['--alluredir', 'report/allure_raw'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure generate report/allure_raw -o ./report/allure_report --clean')
#     #非pycharm，通过allure命令生存服务然后查看--allure  open /report/allure_report
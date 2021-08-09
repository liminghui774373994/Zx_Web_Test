import pytest
import allure
from data_diff import Data_diff

@allure.feature("埋点属性上报")
class Test_params_data:
    params = Data_diff()
    data1 = params.find_parmas_error()


    @allure.story('属性埋点异常')
    @pytest.mark.parametrize('event,params1,params2',data1
                             )
    def test_check(self,event,params1,params2):
                assert params1 == params2


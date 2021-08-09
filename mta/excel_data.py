import pandas as pd

path_target_data = '/Users/beartwo/Documents/数据处理/data_autotest/test_data.xlsx'


class Data_excel():

    def get_excel_event(self):
        df_event_name = pd.read_excel(path_target_data, usecols=[2], names=None)
        df_event_name_li = df_event_name.values.tolist()
        df_event_name_result = []
        for s_li in df_event_name_li:
            df_event_name_result.append(s_li[0])
        #print(df_event_name_result)
        return df_event_name_result

    def get_excel_parmas(self):
        df_event_params = pd.read_excel(path_target_data, usecols=[3], names=None)
        df_event_params_li = df_event_params.values.tolist()
        df_event_params_result = []
        for s_li in df_event_params_li:
            df_event_params_result.append(s_li[0])
        #print(df_event_params_result)
        return df_event_params_result
    '''将Excel中的事件和属性组合成字典'''
    def get_true_data(self):
        df_event_name_result = self.get_excel_event()
        df_event_params_result = self.get_excel_parmas()
        df_event_name1 = set(df_event_name_result)
        true_data = {}
        for word in df_event_name1:
            index_list = [item[0] for item in enumerate(df_event_name_result) if item[1] == word]
            for index in index_list:
                true_data.setdefault(word, []).append(df_event_params_result[index])
        print(true_data)
        return true_data


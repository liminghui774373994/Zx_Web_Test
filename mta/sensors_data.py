import requests


class Data_sensors():

    url = "https://sensorsdata-3.talbrain.com//api/sql/query?token=d1f371d4b2e1736e0b69e61c6ab5f8e0220a5a4e84f12ea195cae1eda46ea3a5&project=Haibian_2019"
    body = {
        'q': "select event,event_params from events where time>= '2020-07-23 18:23:35.085' and time<= '2020-07-23 18:33:53.016' and student_id = 197357 order by event_time desc",
        #'q': "select event,event_params from events where student_id = 197357 order by event_time desc limit 100",
        'format': 'csv'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Connection': 'close'}
    req = requests.post(url, data=body, headers=headers, verify=False)
    req_list = req.text.split('\n')
    dict_key = ['event', 'event_params']
    dict_value = req_list[1:-1]



    def get_sensors_event(self):
        event_value_list = []
        for value in self.dict_value:
            sensors_excel = dict(zip(self.dict_key, value.split('\t')))
            event_value = sensors_excel.get('event')
            event_value_list.append(event_value)
        return event_value_list


    def get_sensors_params(self):
        event_params_value_list = []
        for value in self.dict_value:
            sensors_excel = dict(zip(self.dict_key, value.split('\t')))
            event_params_value = sensors_excel.get('event_params')
            event_params_value_list.append(event_params_value)
        return event_params_value_list


    def get_sensors_data(self):
        dic = {}
        event_value_list  =  self.get_sensors_event()
        event_params_value_list =self.get_sensors_params()
        event_value_list1 = set(event_value_list)
        for word in event_value_list1:
            index_list = [item[0] for item in enumerate(event_value_list) if item[1] == word]
            for index in index_list:
                dic.setdefault(word, []).append(event_params_value_list[index])
        print(dic)
        return dic


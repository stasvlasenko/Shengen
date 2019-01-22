import requests
import json
from pprint import pprint
import datetime

domain = 'izan'
with open('setting.json') as login:
    setting = json.load(login)


def autorized(domain, setting):
    dict = {
        'USER_LOGIN': setting['login'],
        'USER_HASH': setting['hash']
    }

    method = 'private/api/auth.php'
    url = 'https://%s.amocrm.ru/%s?type=json' % (domain, method)

    respond = requests.post(url, json=dict)
    # print(respond.cookies)
    return respond
def list_account(domain, cookies):
    method = 'api/v2/account'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    params = {'with': 'note_types'}
    r = requests.get(url, cookies=cookies)
    return r
def users(domain, cookies):
    method = 'api/v2/account'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    params = 'with=users'
    r = requests.get(url, params=params, cookies=cookies)
    return r
def list_funnel(domain, cookies):
    method = 'api/v2/pipelines'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    # id = {'id': id_voronki}
    r = requests.get(url, cookies=cookies)
    return r.json()
def print_id_funnel(dict_funnel):
    for i in dict_funnel['_embedded']['items']:
        print('Воронка: %s, id: %s' % (
            dict_funnel['_embedded']['items'][i]['name'], dict_funnel['_embedded']['items'][i]['id']))
        for ii in dict_funnel['_embedded']['items'][i]['statuses']:
            print('Этап: %s, id: %s' % (dict_funnel['_embedded']['items'][i]['statuses'][ii]['name'],
                                        dict_funnel['_embedded']['items'][i]['statuses'][ii]['id']))
def list_leads(domain, cookies, status):
    # Показать список лидов в вороке и этапе, с временм изменения таким то
    # Изменить у этих лидов этап
    method = 'api/v2/leads'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    params = {'limit_rows': 100,
              'status': int(status),
              'filter[date_modify][from]': 1545742800,
              'filter[date_modify][to]': 1545750000
              }

    r = requests.get(url, params=params, cookies=cookies)
    return r
def select_lead_time_update(dict_leads, time_start, time_end):
    list_leads_in_time = {}
    i = 0
    for lead in dict_leads['_embedded']['items']:
        print(lead['updated_at'])
        if time_start <= lead['updated_at'] <= time_end:
            list_leads_in_time = {i: [{'id': lead['id'],
                                       'name': lead['name'],
                                       'updated_at': lead['updated_at'],
                                       'status_id': 23743182

                                       }]}
            i += 1
    return list_leads_in_time
def update_lead_status(dict_leads, domain, cookies):
    #for i in dict_leads['_embedded']['items']:
        method = 'api/v2/leads'
        url = 'https://%s.amocrm.ru/%s' % (domain, method)

        headers = {'Content-type': 'application/json',  # Определение типа данных
                   'Accept': 'application/json',
                   'Content-Encoding': 'utf-8'}
        data = {'update': dict_leads['_embedded']['items']}
        """
        data = {'update': [{
                    'id': i['id'],
                    'name': i['name'],
                    'updated_at': i['updated_at'],
                    'status_id': i['status_id']
        }]}
        """

        data = json.dumps(data)

        r = requests.post(url, data=data, cookies=cookies, headers=headers)
        print(r.json())

# Авторизуемся и сохраняем куки для дальнейших вызовов
cookies = autorized(domain, setting).cookies

# Получим список воронок и статусов, чтобы выбрать куда переносить
#dict_funnel = list_funnel(domain, cookies)
#print_id_funnel(dict_funnel)

#Цикл который остановит скрипт, когда кончатся сделки
list_status = True
while list_status == True:
    # Спрашиваем где выбирать сделки
    print('Введите номер этапа, с которого забрать сделки: 19123065')
    status = 19123065
    dict_leads = list_leads(domain, cookies, status).json()

    print('Количество сделок выбрано:', len(dict_leads['_embedded']['items']))
    if len(dict_leads['_embedded']['items']) < 100:
        list_status = False

    for i in dict_leads['_embedded']['items']:
        i['status_id'] = 23743182

    update_lead_status(dict_leads, domain, cookies)





"""
# Из даты в таймштамп
print('Выбираем интервал дат для лидов')
start = datetime.datetime(2018, 12, 19, 17, 30, 15).timestamp()
stop = datetime.datetime(2018, 12, 19, 19, 30, 15).timestamp()
search_data = datetime.datetime.fromtimestamp(1545202333)
print('Дата старта %s дата финиша %s, базовая дата:%s' % (start, stop, search_data))
"""

"""
list_lead_time_update = select_lead_time_update(dict_leads, 1545202300, 1545202400)
print('финальный список тест')
print(list_lead_time_update[1])
#print_id_funnel(domain, cookies)





response = update_lead_status(list_lead_time_update, 23743182, domain, cookies)
pprint(response.json())
"""
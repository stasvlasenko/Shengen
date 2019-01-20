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
    #print(respond.cookies)
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
    #id = {'id': id_voronki}
    r = requests.get(url, cookies=cookies)
    return r
def print_id_funnel(domain, cookies):
    dict_funnel = list_funnel(domain, cookies).json()

    for i in dict_funnel['_embedded']['items']:
        print('Воронка: %s, id: %s' % (
        dict_funnel['_embedded']['items'][i]['name'], dict_funnel['_embedded']['items'][i]['id']))
        for ii in dict_funnel['_embedded']['items'][i]['statuses']:
            print('Этап: %s, id: %s' % (dict_funnel['_embedded']['items'][i]['statuses'][ii]['name'],
                                        dict_funnel['_embedded']['items'][i]['statuses'][ii]['id']))
def list_leads(domain, cookies):
    # Показать список лидов в вороке и этапе, с временм изменения таким то
    # Изменить у этих лидов этап
    method = 'api/v2/leads'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    params = {'limit_rows': 2,
              'status': 19123065,
              }
    r = requests.get(url, params=params, cookies=cookies)
    return r
def select_lead_time_update (dict_leads, time_start, time_end):
    list_leads_in_time = []
    for lead in dict_leads['_embedded']['items']:
        print(lead['updated_at'])
        if time_start <= lead['updated_at'] <= time_end:
            list_leads_in_time.append(lead['id'])
    return list_leads_in_time

#Авторизуемся и сохраняем куки для дальнейших вызовов
cookies = autorized(domain, setting).cookies
#dict_users = users(domain, cookies).json()
#dict_account = list_account(domain, cookies).json()
dict_funnel = list_funnel(domain, cookies).json()
dict_leads = list_leads(domain, cookies).json()

print('Массив лидов:')
pprint(dict_leads['_embedded']['items'])

#Из даты в таймштамп
start = datetime.datetime(2018,12,19,17,30,15).timestamp()
stop = datetime.datetime(2018,12,19,19,30,15).timestamp()
search_data = datetime.datetime.fromtimestamp(1545202333)
print('Дата старта %s дата финиша %s, базовая дата:%s' %(start, stop, search_data))


list_lead_time_update = select_lead_time_update(dict_leads, 1545202300, 1545202400)
print(list_lead_time_update)
print_id_funnel(domain, cookies)

def update_lead_status (list_lead, change_status, domain, cookies):
    method = 'api/v2/leads'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
    data = {'update': [{
                      'id': list_lead[0],
                      'status_id': change_status
                  }]
            }
    data = json.dumps(data)
    print(data)

    r = requests.post(url, data=data, cookies=cookies, headers=headers)
    return r

response = update_lead_status(list_lead_time_update, 23743182, domain, cookies)
print(response.json())

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
def list_funnel(domain, cookie):
    method = 'api/v2/pipelines'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    #id = {'id': id_voronki}
    r = requests.get(url, cookies=cookies)
    return r
def list_leads(domain, cookie):
    # Показать список лидов в вороке и этапе, с временм изменения таким то
    # Изменить у этих лидов этап
    method = 'api/v2/leads'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    params = {'limit_rows': 2,
              'status': 19123065}
    r = requests.get(url, params=params, cookies=cookies)
    return r


#Авторизуемся и сохраняем куки для дальнейших вызовов
cookies = autorized(domain, setting).cookies

#dict_users = users(domain, cookies).json()

#dict_account = list_account(domain, cookies).json()
dict_funnel = list_funnel(domain, cookies).json()
dict_leads = list_leads(domain, cookies).json()

print('Данные о воронках:')
for i in dict_funnel['_embedded']['items']:
    print(dict_funnel['_embedded']['items'][i])

print('Массив лидов:')
#for i in dict_leads['_embedded']['items']:
#    print(dict_leads['_embedded']['items'][i])

pprint(dict_leads['_embedded']['items'])

#Из даты в таймштамп
start = datetime.datetime(2018,12,19,17,30,15).timestamp()
stop = datetime.datetime(2018,12,19,19,30,15).timestamp()
search_data = datetime.datetime.fromtimestamp(1545202333)
print('Дата старта %s дата финиша %s, базовая дата:%s' %(start, stop, search_data))
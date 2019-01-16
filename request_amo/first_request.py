import requests
import json
from pprint import pprint

domain = 'izan'

def autorized(domain):
    dict = {
        'USER_LOGIN': 'eadorf@gmail.com',
        'USER_HASH': '2f9665f414a2a89df40f49be4bf17ea1fa5db0da'
    }

    method = 'private/api/auth.php'
    url = 'https://%s.amocrm.ru/%s?type=json' % (domain, method)

    respond = requests.post(url, json=dict)
    #print(respond.cookies)
    return respond

def users(domain, cookies):
    autorized(domain)
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
    method = 'api/v2/leads'
    url = 'https://%s.amocrm.ru/%s' % (domain, method)
    id = {'id': 123123}
    r = requests.get(url, params=id, cookies=cookies)
    return r

#Авторизуемся и сохраняем куки для дальнейших вызовов
cookies = autorized(domain).cookies

#dict_users = users(domain, cookies).json()

dict_funnel = list_funnel(domain, cookies).json()
dict_leads = list_leads(domain, cookies).json()

print('Данные о воронках:')
for i in dict_funnel['_embedded']['items']:
    print(dict_funnel['_embedded']['items'][i])
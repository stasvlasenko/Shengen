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

#Авторизуемся и сохраняем куки для дальнейших вызовов
cookies = autorized(domain).cookies

dict_users = users(domain, cookies).json()
pprint(dict_users)



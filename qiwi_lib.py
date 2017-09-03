# -*- coding: utf-8 -*-

import requests
import json

api_access_token = '49109c93639af46bfdb8bc9bacfb8d9d' # токен можно получить здесь https://qiwi.com/api полученый токен вставить в ''

headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + api_access_token}

qiwi_autoriz = requests.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled', headers=headers)
qiwi_paymates = requests.get('https://edge.qiwi.com/payment-history/v1/persons/380685124286/payments?rows=10&operation=ALL', headers=headers)

last_upd = qiwi_paymates.json()
for i in range(0, 10):
    money_comment = last_upd['data'][i]['comment']
    print(money_comment)
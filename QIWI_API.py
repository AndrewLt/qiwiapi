import requests


def qiwi_pay_check():
    qiwi_number = 'PHONE NUMBER'
    api_access_token = 'API TOKEN' #https://qiwi.com/api
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 
               'Authorization': 'Bearer ' + api_access_token}
    try:
        qiwi_autoriz = requests.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled',
                                    headers=headers)
        qiwi_paymates = requests.get('https://edge.qiwi.com/payment-history/v1/persons/' + str(
            qiwi_number) + '/payments?rows=10&operation=IN', headers=headers)   #rows = 10 - количество транзакций; operation=IN входящие транзакции
        last_upd = qiwi_paymates.json()
        for i in range(0, 10):
            try:
                print(last_upd)
            except:
                print('Index out of range')
    except:
        print('Ошибка в подключении или авторизации QIWI_API')

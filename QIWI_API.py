import requests


def qiwi_requisites(sum_of_pay):
    qiwi_walets_list = Wallets.query.filter(Wallets.wallet_name == 'QIWI').all()
    try:
        for list in qiwi_walets_list:
            api_access_token = str(list.api_key)
            qiwi_number = str(list.additional_column)
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                       'Authorization': 'Bearer ' + api_access_token}
            balance = 0
            try:
                qiwi_autoriz = requests.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled',
                                            headers=headers)
                qiwi_balance = requests.get('https://edge.qiwi.com//funding-sources/v2/persons/'
                                            + str(qiwi_number) + '/accounts', headers=headers)
                last_upd = qiwi_balance.json()
                if last_upd['accounts'][0]['balance']['currency'] == 643:
                    balance = last_upd['accounts'][0]['balance']['amount']
                    if float(balance) + float(sum_of_pay) < 14500:
                        return qiwi_number
                else:
                    if last_upd['accounts'][1]['balance']['currency'] == 643:
                        balance = last_upd['accounts'][1]['balance']['amount']
                        if float(balance) + float(sum_of_pay) < 14500:
                            return qiwi_number
            except:
                print('Ошибка в подключении или загрузке баланса!')
    except:
        print('Error in qiwi_requisites, pay_methods')

def qiwi_pay_check(user_id):
    user = AAllUsers.query.filter(AAllUsers.chat_id == str(user_id)).first()
    wallet = Wallets.query.filter(Wallets.additional_column == str(user.Qiwi)).first()
    api_access_token = str(wallet.api_key)
    qiwi_number = str(wallet.additional_column)
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + api_access_token}
    value_of_pay = user.Free_Column
    comment = user.Free_Column_Two
    try:
        qiwi_autoriz = requests.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled',
                                    headers=headers)
        qiwi_paymates = requests.get('https://edge.qiwi.com/payment-history/v1/persons/' + str(
            qiwi_number) + '/payments?rows=10&operation=IN', headers=headers)
        last_upd = qiwi_paymates.json()
        for i in range(0, 10):
            try:
                if last_upd['data'][i]['comment'] == str(comment) and float(last_upd['data'][i]['sum']['amount']) >= float(value_of_pay):
                    return True
            except:
                print('Index out of range')
    except:
        print('Ошибка в подключении и авторизации QIWI_API')

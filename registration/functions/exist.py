import requests


def is_exist(user_id, link):
    response = requests.get(link).json()
    for i in response:
        if i['user_id'] == user_id:
            return False
    return True


def check_nickname(nickname, link):
    response = requests.get(link).json()
    for i in response:
        if i['nickname'] == nickname:
            return False
    return True


def save_data(user_id, fullname, nickname, phone_number, link):
    response = requests.get(link).json()
    a = len(response) + 1
    data = {
        'id': a,
        'user_id': user_id,
        'fullname': fullname,
        'nickname': nickname,
        'phone_number': phone_number,
        'status': 'lose'
    }
    response = requests.post(link, data=data)
    if response.status_code == 201:
        return True
    return False

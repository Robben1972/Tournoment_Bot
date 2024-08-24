import random

import requests


def find_opponents(link):
    response = requests.get(link).json()
    players = [player['nickname'] for player in response if player['status'] == 'lose']
    opponents = []
    while len(players) > 1:
        player1 = random.choice(players)
        players.remove(player1)
        player2 = random.choice(players)
        players.remove(player2)
        opponents.append(f"{player1}-{player2}")
    if players:
        opponents.append(f"{players[0]}-win")
    return opponents


def choose_winner(nick, link, winner_api, reward_link):
    response = requests.get(link).json()
    players = [player['nickname'] for player in response if player['status'] == 'lose']
    if len(players) != 2:
        for i in response:
            if i['nickname'] == nick:
                i['status'] = 'win'
                requests.patch(f'{link}{i["id"]}/', {'status': 'win'})
                data = {
                    'user_id': i['user_id'],
                    'fullname': i['fullname'],
                    'nickname': i['nickname'],
                }
                requests.post(winner_api, data=data)
                break
    else:
        for i in response:
            if i['nickname'] == nick:
                requests.patch(f'{link}{i["id"]}/', {'status': '1st'})
                requests.post(reward_link,
                              {'user_id': i['user_id'], 'fullname': i['fullname'], 'nickname': i['nickname'],
                               'status': '1st'})
                data = {
                    'user_id': i['user_id'],
                    'fullname': i['fullname'],
                    'nickname': i['nickname'],
                }
                requests.post(winner_api, data=data)
            elif i['status'] == 'lose':
                requests.patch(f'{link}{i["id"]}/', {'status': '2nd'})
                requests.post(reward_link,
                              {'user_id': i['user_id'], 'fullname': i['fullname'], 'nickname': i['nickname'],
                               'status': '2nd'})


def delete_users(link, delete_link, reward_link):
    response = requests.get(link).json()
    if len(response) > 4:
        for i in response:
            if i['status'] == 'lose':
                url = f"{link}{i['id']}"
                requests.post(delete_link,
                              {'user_id': i['user_id'], 'fullname': i['fullname'], 'nickname': i['nickname']})
                requests.delete(url)
            else:
                requests.patch(f'{link}{i["id"]}/', {'status': 'lose'})
    else:
        players = [player['nickname'] for player in response if player['status'] == 'win']
        if len(players) == 2:
            for i in response:
                if i['status'] == 'lose':
                    requests.patch(f'{link}{i["id"]}/', {'status': '3rd'})
                    requests.post(reward_link,
                                  {'user_id': i['user_id'], 'fullname': i['fullname'], 'nickname': i['nickname'],
                                   'status': '3rd'})
                else:
                    requests.patch(f'{link}{i["id"]}/', {'status': 'lose'})


def send_notification(player1, player2, link1, link2):
    response = requests.get(link2).json()
    a = 0
    b = 0
    if player1 != 'win' or player2 != 'win':
        for i in response:
            if i['nickname'] == player1:
                a = i['user_id']
            elif i['nickname'] == player2:
                b = i['user_id']
        data1 = {
            'user_id': a,
            'nickname': player1,
            'opponent_nickname': player2,
        }
        requests.post(link1, data1)

        data1 = {
            'user_id': b,
            'nickname': player2,
            'opponent_nickname': player1,
        }
        requests.post(link1, data1)

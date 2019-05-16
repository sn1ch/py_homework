from pprint import pprint
from urllib.parse import urlencode
import requests

VK_API = 6983631
BASE_URL = 'https://oauth.vk.com/authorize'

authorization = {
    'client_id': VK_API,
    'display': 'popup',
    'scope': 'friends, status',
    'response_type': 'token',
    'v': '5.95'

}

pprint('?'.join((BASE_URL, urlencode(authorization))))

TOKEN = '5a36bca8873ba7b92033f069d3ec032acf010d408279f51b97d7a47a96f4c3b54aa2c6998f7e7a4678ec7'


class User:
    def __init__(self, token, user_id=17820325):
        self.token = token
        self.user_id = user_id

    def get_params(self):
        params = {
            'access_token': self.token,
            'user_id': self.user_id,
            'v': '5.95',
            'order': 'hints',
            'fields': 'nickname'
        }
        return params

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = other.user_id
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        mutual_friends_dict = response.json()
        mutual_friends = []
        for friends in mutual_friends_dict.values():
            for friend in friends:
                mutual_friends.append(User(TOKEN, user_id=friend))
        return mutual_friends

    def __repr__(self):
        URL_VK = 'https://vk.com/id'
        USER_ID = self.user_id
        return ''.join([URL_VK, str(USER_ID)])


Serg = User(TOKEN)
Diana = User(TOKEN, user_id='37893810')

print(f'Список общих друзей двух пользователей Serg и Diana {Serg & Diana}')
print(f'Тип объекта в списке возвращаемого после поиска обших друзей двух пользователей {type((Serg & Diana)[1])}.')

print(f'Ссылка на пользователя Serg в сети VK: {Serg}')

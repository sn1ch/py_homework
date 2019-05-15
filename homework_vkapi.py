from pprint import pprint
from urllib.parse import urlencode
import requests

VK_API = 6983631
BASE_URL = 'https://oauth.vk.com/authorize'

avtorizaciz = {
    'client_id': VK_API,
    'display': 'popup',
    'scope': 'friends, status',
    'response_type': 'token',
    'v': '5.95'

}

pprint('?'.join((BASE_URL, urlencode(avtorizaciz))))

# TOKEN = 'bcc1fffe4f135e4040b798d55ffe2784ae559cda951b392de3d4e0134d4f7bbc656143693e8e8984c8edc'
TOKEN = '668021e03117339448c445050489428ce095b2dcf8f0c01472ef7344c384d770dd51f34037afef29110cc'

params1 = {
    'access_token': TOKEN,
    'v': '5.95',
    'order': 'hints',
    'fields': 'nickname'
}


# resp2 = requests.get('https://api.vk.com/method/friends.get', params1)


# pprint(resp2)
# pprint(resp2.text)
# pprint(resp2.json())


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
        resp3 = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return resp3.json()

    def get_friendlist(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

    def a(self):
        params = self.get_params()
        params['source_uid'] = '4417893'
        params['target_uid'] = '37893810'
        resp3 = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return resp3.json()


serg = User(TOKEN)
# pprint(serg.get_friendlist())
pprint(serg.a())
url = 'https://vk.com/id'
id = '37893810'
diana = User(TOKEN, user_id='37893810')
# pprint(serg & diana)

a = serg & diana
list = []
for i in a.values():
    for k in i:
        list.append(User(TOKEN, user_id=k))
print(list)
print(list[1].get_friendlist())





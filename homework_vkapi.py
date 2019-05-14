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
    # 'redirect_uri': 'https://sad.com/'

}

pprint('?'.join((BASE_URL, urlencode(avtorizaciz))))

TOKEN = 'bcc1fffe4f135e4040b798d55ffe2784ae559cda951b392de3d4e0134d4f7bbc656143693e8e8984c8edc'

params = {
    'access_token': TOKEN,
    'v': '5.95'
}

resp = requests.get('https://api.vk.com/method/status.get', params)
# pprint(resp)
# pprint(resp.text)
# pprint(resp.json())
# pprint(params)
# params['text'] = 'olool'
# pprint(params)

params1 = {
    'access_token': TOKEN,
    'v': '5.95',
    'order': 'hints',
    'fields': 'nickname'
}
resp2 = requests.get('https://api.vk.com/method/friends.get', params1)
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

    def get_friendlist(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

serg = User(TOKEN)
pprint(serg.get_friendlist())

# diana = User(TOKEN, user_id='37893810')
# pprint(diana.get_friendlist())

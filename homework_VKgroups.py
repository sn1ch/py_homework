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
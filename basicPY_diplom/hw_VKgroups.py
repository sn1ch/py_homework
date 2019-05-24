from pprint import pprint
from urllib.parse import urlencode
import requests
import time
import json

VK_API = 6983631
BASE_URL = 'https://oauth.vk.com/authorize'

authorization = {
    'client_id': VK_API,
    'display': 'popup',
    'scope': 'friends, groups',
    'response_type': 'token',
    'v': '5.95'
}

pprint('?'.join((BASE_URL, urlencode(authorization))))

# TOKEN = '8f78e37ecd898e6302dd83dcd8956856f33e71b8d579c041b568e6b1f994e902c4f16edc0e9df94a122fa'  # Я
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'  # ЖЕНЯ


class User:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        params = {
            'access_token': self.token,
            'v': '5.95',
            'fields': 'nickname'
        }
        return params

    def get_user_id(self, user):
        params = self.get_params()
        params['user_ids'] = user
        response = requests.get('https://api.vk.com/method/users.get', params)
        user_info = response.json()
        for items in user_info['response']:
            user_id = items['id']
            return user_id

    def get_groups(self, user_id):
        params = self.get_params()
        params['user_id'] = user_id
        params['extended'] = '0'
        response = requests.get('https://api.vk.com/method/groups.get', params)
        print('...')
        time.sleep(0.34)
        groups_list_json = response.json()
        groups_list = []
        for group_id in groups_list_json['response']['items']:
            groups_list.append(group_id)
        return groups_list

    def get_friends_groups(self, group_id):
        params = self.get_params()
        params['group_id'] = group_id 
        params['filter'] = 'friends'
        response = requests.get('https://api.vk.com/method/groups.getMembers', params)
        print('...')
        time.sleep(0.34)
        return response.json()

    def no_friends_groups_id(self, total_groups):
        no_friends_groups_list = []
        for group in total_groups:
            if self.get_friends_groups(group)['response']['count'] == 0:
                no_friends_groups_list.append(group)
        return no_friends_groups_list

    def no_friends_groups_result(self, no_friends_groups_list):
        params = self.get_params()
        params['group_ids'] = ''
        for i in range(len(no_friends_groups_list)):
            if i == 0:
                params['group_ids'] += str(no_friends_groups_list[i])
            else:
                params['group_ids'] += ', ' + str(no_friends_groups_list[i])
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        print('...')
        time.sleep(0.34)
        return response.json()

    def get_friends(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()


def write_file(path, data):
    with open(path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4, separators=(',', ': '))


def get_closed_and_banned_friends(friends, data):
    for i in friends['response']['items']:
        try:
            if i['deactivated'] == 'deleted' or i['deactivated'] == 'banned':
                data.setdefault('closed_friends', [])
                data['closed_friends'].append(
                    {'id': i['id'], 'first_name': i['first_name'], 'last_name': i['last_name'],
                     'deactivated': i['deactivated']})

        except KeyError:
            if i['is_closed']:
                data.setdefault('closed_friends', [])
                data['closed_friends'].append(
                    {'id': i['id'], 'first_name': i['first_name'], 'last_name': i['last_name'],
                     'is_closed': i['is_closed']})
    data.setdefault('count_closed_friends', len(data['closed_friends']))
    return data


if __name__ == '__main__':
    user = input('Ввеите ID или коротий адрес страницы: ')
    user1 = User(TOKEN)
    user_id = user1.get_user_id(user)
    total_groups = user1.get_groups(user_id)
    no_friends_groups_list = user1.no_friends_groups_id(total_groups)
    no_friends_group = user1.no_friends_groups_result(no_friends_groups_list)
    friends = user1.get_friends()
    data = get_closed_and_banned_friends(friends, no_friends_group)
    write_file('VKgroups.json', data)

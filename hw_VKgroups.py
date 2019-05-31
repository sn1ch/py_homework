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

# TOKEN = 'c06bb1e0f991663abe4baf54d57b79cc7123a2406e396139dfebd1b05c2130ffbadb7b6ae7a82eedfa576'  # Я
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
        print(groups_list_json)
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

    def get_friends(self, user_id):
        params = self.get_params()
        params['user_id'] = user_id
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

    def s(self, groups):
        params = self.get_params()
        for group in groups['response']:
            print(group['items'])

    def isM(self, group_id, user_id):
        params = self.get_params()
        params['group_id'] = group_id
        params['user_id'] = user_id
        response = requests.get('https://api.vk.com/method/groups.isMember', params)
        print('...')
        time.sleep(0.34)
        return response.json()


def write_file(path, data):
    with open(path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4, separators=(',', ': '))


def get_closed_and_banned_friends(friends):
    total_closed_and_banned_friends = 0
    closed_and_banned_friends = []
    for i in friends['response']['items']:
        try:
            if i['deactivated'] == 'deleted' or i['deactivated'] == 'banned':
                closed_and_banned_friends.append(
                    {'id': i['id'], 'first_name': i['first_name'], 'last_name': i['last_name'],
                     'deactivated': i['deactivated']})
                total_closed_and_banned_friends += 1

        except KeyError:
            if i['is_closed']:
                closed_and_banned_friends.append(
                    {'id': i['id'], 'first_name': i['first_name'], 'last_name': i['last_name'],
                     'is_closed': i['is_closed']})
                total_closed_and_banned_friends += 1
    closed_and_banned_friends.append({'total_closed_and_banned_friends': total_closed_and_banned_friends})
    return closed_and_banned_friends


if __name__ == '__main__':
    user = 'sn1ch'  # тут сделать инпут 171691064 eshmargunov sn1ch 17820325
    # user = input('Введите ID или коротий адрес страницы: ')
    user1 = User(TOKEN)
    user_id = user1.get_user_id(user)
    total_groups = user1.get_groups(user_id)
    no_friends_groups_list = user1.no_friends_groups_id(total_groups)
    no_friends_group = user1.no_friends_groups_result(no_friends_groups_list)
    friends = user1.get_friends(user_id)
    pprint(friends)
    # pprint(get_closed_and_banned_friends(friends))
    # write_file('VKgroups.json', no_friends_group)
    # user1.s(total_groups)
    for i in total_groups:
        for k in friends['response']['items']:
            # print(user1.isM(i, k['id']))
            a = user1.isM(i, k['id'])
            if a['response'] == 1:
                print(k['id'], ' состоит в груупе ', i)

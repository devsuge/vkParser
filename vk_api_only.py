import requests

API_URL = 'https://api.vk.com/method'
API_VERSION = '5.131'


def get_friends(token, u_id):
    METHOD_URL = API_URL + '/friends.get'

    response = requests.get(METHOD_URL,
                            {'access_token': token,
                             'user_id': u_id,
                             'order': 'name',
                             'fields': 'nickname, country, city, bdate, sex',
                             'v': API_VERSION}).json()

    error = response.get('error', {})
    if error:
        code = error.get('error_code', 'Unknown error')
        msg = error.get('error_msg', '-1')
        raise ValueError(f'{msg} [Error code: {code}]')

    response_data = response.get('response', {})

    raw_data = response_data.get('items', [])
    count = response_data.get('count') // 5000
    if count > 1:
        for i in range(1, count + 1):
            raw_data += requests.get(METHOD_URL,
                                     {'access_token': token,
                                      'user_id': u_id,
                                      'order': 'name',
                                      'fields': 'nickname, country, city, bdate, sex',
                                      'offset': i * 5000,
                                      'v': API_VERSION}).json().get('response', {}).get('items', [])
    return raw_data

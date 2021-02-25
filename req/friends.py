import requests
from pprint import pprint
from datetime import datetime
from collections import Counter

ACCESS_TOKEN = '422ac984422ac984422ac98463425c52f74422a422ac984221d1c223d90e46a32b2839a'

def calc_age(uid):
    url = f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}'
    r = requests.get(url)
    json_data = r.json()
    if not json_data:
        return f'User "{uid}" not found!'
    user_id = json_data['response'][0]['id']
    url = f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}&user_id={user_id}&fields=bdate'
    r = requests.get(url)
    json_data = r.json()
    
    if not json_data:
        return f'User\'s "{uid}" friends not found!'
    
    if 'response' not in json_data:
        return f'User\'s "{uid}" friends not found!'
    
    friends_list = json_data['response']['items']

    return sorted([(age,n) for age,n in dict(Counter([
        datetime.now().year - int(f['bdate'].split('.')[2]) 
        for f in friends_list 
        if len(f.get('bdate','').split('.'))==3
    ])).items()], key=lambda x: (x[1], -x[0]), reverse=True)

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)

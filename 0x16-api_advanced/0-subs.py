#!/usr/bin/python3
""" module to test reddit api"""
from requests import get, post
from requests.auth import HTTPBasicAuth


def remove_zeroes(data):
    """function to remove zeroes from a list"""
    non_zero_values = []
    for item in data:
        if isinstance(item, list):
            non_zero_values.extend(remove_zeroes(item))
        elif item != 0:
            non_zero_values.append(item)
    return non_zero_values


def search_json(search_data, searched_key):
    """function to search for a key in a json"""
    if isinstance(search_data, dict):
        if searched_key in search_data:
            val = search_data.get(searched_key)
            if val != 0:
                return val
        return [search_json(search_data[key],
                            searched_key) for key in search_data.keys()]
    elif isinstance(search_data, list):
        for item in search_data:
            return search_json(item, searched_key)
    else:
        return 0


def number_of_subscribers(subreddit):
    """function to get the number of subscribers for a given subreddit
    @subreddit: the subreddit to search for
    """
    full_url = 'https://oauth.reddit.com/r/' + subreddit + ''

    headers = {
        'User-Agent': 'script:test.api:v1 (by /u/5miiss96)',
        'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI\
1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdW\
NZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NTI5NTE2\
LjExNTc5NywiaWF0IjoxNjk5NDQzMTE2LjExNTc5NywianRpIjoiMWRYMmZKSXp0\
V3BBQjJCdHpGY21xMUoxZVc5aUZnIiwiY2lkIjoiUllhZUYzcWtIcTZvRmFwZ0k3cGI\
zUSIsImxpZCI6InQyX21qNGJoNjdncyIsImFpZCI6InQyX21qNGJoNjdncyIsImxjYSI\
6MTY5ODI2NzU4Mzc5OSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8i\
Ojl9.CZP6Do2857JfHiYvt0giq8yTbym3tkPN3qC1ClYrpzKCYb6pNDdT1L45EaM8c17zWSg\
-MNnyAyaZkRDE6ddb6tnL6pvu6EHHppfrYqdSK9v4M7edxcueWb_taYlpKFDO3CMbMtGbJTtPX\
5C3tjgklw3RbPd24K65GoPNLdvxX6KFB1cRb6nGS4sy0N_ooIfr9d909xtpNA5OjDZtksr3qpYrNp\
VRiEKeJ_H95Oxl_FNHuFFdSxNo30pvvLxvh2SEhhqoofg_C5mzsKo3-VZrYWzTk1zRFa8RGxrlJs0Wx\
Dq9DemXs-aIjVE_g613LCbuN3TnKR8nxID9EgB1GjZqOA'
    }
    response = get(full_url, headers=headers)
    if response.status_code != 200:
        return 0
    data = search_json(response.json(), 'subreddit_subscribers')
    ls = remove_zeroes(data)
    if len(ls) > 0:
        return ls[0]
    return 0


def get_token():
    """function to get the token for the script using my credentials"""
    client_auth = HTTPBasicAuth('RYaeF3qkHq6oFapgI7pb3Q',
                                'DKGtb-pj9jH_j-1_eNZSK752-io_tw')
    post_data = {"grant_type": "password",
                 "username": "5miiss96",
                 "password": "a37831654"}
    headers = {
        'User-Agent': 'script:test.api:v1 (by /u/5miiss96)'
    }
    response = post("https://www.reddit.com/api/v1/access_token",
                    auth=client_auth, data=post_data,
                    headers=headers)
    return response.json().get('access_token')


if __name__ == '__main__':
    pass

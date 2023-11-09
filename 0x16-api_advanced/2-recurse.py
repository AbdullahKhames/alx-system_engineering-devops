#!/usr/bin/python3
""" module to test reddit api"""
from requests import get


def recurse(subreddit, hot_list=[], last_after=None):
    """function to get the number of subscribers for a given subreddit
    @subreddit: the subreddit to search for
    """
    titles = []
    titles.extend([post.get('title') for post in hot_list])
    full_url = 'https://oauth.reddit.com/r/' + subreddit + '/hot'
    after = hot_list[-1].get('name') if len(hot_list) > 0 else None
    if last_after is not None and last_after == after:
        return titles
    params = {
        'raw_json': 1,
        'limit': 100,
        'after': after,
    }
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
    response = get(full_url,
                   headers=headers,
                   params=params,
                   allow_redirects=False)
    if response.status_code != 200:
        return None
    children = []
    for child in response.json().get('data').get('children'):
        children.append(child.get('data'))
    hot_list.extend(children)
    items = response.request.url.split('after=')
    if len(items) > 1:
        last_after = items[1]
    return recurse(subreddit, hot_list, last_after=last_after)


if __name__ == '__main__':
    print(recurse('programming'))

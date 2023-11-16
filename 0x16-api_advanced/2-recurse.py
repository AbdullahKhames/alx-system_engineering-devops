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
        'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NjE3Njg5LjQ1MzY2NCwiaWF0IjoxNjk5NTMxMjg5LjQ1MzY2NCwianRpIjoiXzBCQVFKckxTanhFZkI3VnhNQVJsdjRGbkg1SUVBIiwiY2lkIjoiUllhZUYzcWtIcTZvRmFwZ0k3cGIzUSIsImxpZCI6InQyX21qNGJoNjdncyIsImFpZCI6InQyX21qNGJoNjdncyIsImxjYSI6MTY5ODI2NzU4Mzc5OSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.ZHx1PUlDBAey4EQ_CAzl69QSw9rivCNvbPTsCRVZWIpurS1CoEoFMF2V_H2je1nmtVnhx2KoAdEHf2nG-5bMFBj3LDIu17dnUroxXKWP5HW2U-NgV6qP9P4oNPuDQOFT_A6-EdjRL8azfBzQu_aSQr36LNczP5EOkoOx_YLljmB1pqIhRSoxZY3vY4CDZVRXWQNiMTe9UBkn53pVDhpj4rxIrVcgJzuhqd0-n9jPc757pKWcl_VjUiTQKcBn_BJXzxpRCDNHOYPqA6O0B93XKPrt1Bpv-Iy8s3oSzudZS52NjScEmadXpnlTaZSdqCZ9mG1_DHEs5DIPkIrxDYNcxQ'

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

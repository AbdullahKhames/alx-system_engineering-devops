#!/usr/bin/python3
""" module to test reddit api"""
from requests import get


def search_json(search_data, searched_key):
    """function to search for a key in a json"""
    result = []
    if isinstance(search_data, dict):
        for key, value in search_data.items():
            if key == searched_key:
                result.append(value)
            else:
                result.extend(search_json(value, searched_key))
    elif isinstance(search_data, list):
        for item in search_data:
            result.extend(search_json(item, searched_key))
    return result


def top_ten(subreddit):
    """function to get the number of subscribers for a given subreddit
    @subreddit: the subreddit to search for
    """
    full_url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    params = {
        'raw_json': 1,
        'limit': 9,
    }
    headers = {
        'User-Agent': 'script:test.api:v1 (by /u/5miiss96)',
    }
    response = get(full_url,
                   headers=headers,
                   params=params)
    if response.status_code != 200:
        print(None)
    data = search_json(response.json(), 'title')
    for title in data:
        print(title)


if __name__ == '__main__':
    top_ten('programming')

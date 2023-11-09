#!/usr/bin/python3
""" module to test reddit api"""
from requests import get


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
    full_url = 'https://www.reddit.com/r/' + subreddit + '.json'

    headers = {
        'User-Agent': 'script:test.api:v1 (by /u/5miiss96)',
    }
    response = get(full_url, headers=headers)
    if response.status_code != 200:
        return 0
    data = search_json(response.json(), 'subreddit_subscribers')
    ls = remove_zeroes(data)
    if len(ls) > 0:
        return ls[0]
    return 0


if __name__ == '__main__':
    number_of_subscribers('programming')

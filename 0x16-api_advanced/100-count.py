#!/usr/bin/python3
""" module to test reddit api"""
from requests import get


def recurse(subreddit, hot_list=[], last_after=None):
    """function to get the number of subscribers for a given subreddit
    @subreddit: the subreddit to search for
    """
    titles = []
    titles.extend([post.get('title') for post in hot_list])
    full_url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
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


def count_word(titles, searched_key):
    """function to count the number of times a word appears in a list of titles"""
    if titles is None:
        return None
    count = 0
    for title in titles:
        for word in title.split():
            if word.lower() == searched_key.lower():
                count += 1
    return count


def get_swap_indices(new_dict):
    last_val = None
    last_k = None
    swap_indices = []
    for i, (k, v) in enumerate(new_dict.items()):
        if last_val is not None and v == last_val and k.lower() < last_k.lower():
            swap_indices.extend([i - 1, i])
        last_val, last_k = v, k
    return swap_indices


def count_similar(new_dict):
    last_k = None
    for k in list(new_dict.keys()):
        if last_k is not None and k.lower() == last_k.lower():
            new_dict[k] += new_dict[last_k]
            del new_dict[last_k]
        last_k = k


def swap(new_dict, i, j):
    tups = list(new_dict.items())
    tups[i], tups[j] = tups[j], tups[i]


def parse_dict(word_dict):
    new_dict = dict(sorted(word_dict.items(), key=lambda tup: (tup[1]), reverse=True))
    count_similar(new_dict)
    new_dict = dict(sorted(new_dict.items(), key=lambda tup: (tup[1]), reverse=True))
    swap_indices = get_swap_indices(new_dict)
    for i, j in zip(swap_indices[::2], swap_indices[1::2]):
        swap(new_dict, i, j)
    return new_dict


def count_similar1(word_dict):
    # Sort keys (case-insensitive)
    sorted_items = sorted(word_dict.items(), key=lambda tup: tup[0].lower())

    # Merge items with similar keys
    new_dict = {}
    for k, v in sorted_items:
        k_lower = k.lower()
        if k_lower in new_dict:
            new_dict[k_lower] += v
        else:
            new_dict[k_lower] = v

    return new_dict


def parse_dict1(word_dict):
    word_dict = count_similar1(word_dict)

    return dict(sorted(word_dict.items(), key=lambda tup: (-tup[1], tup[0].lower())))


def count_words(subreddit, word_list):
    word_dict = {}
    titles = recurse(subreddit)
    for word in word_list:
        count = count_word(titles, word)
        if count != 0:
            word_dict[word] = count
    new_dict = parse_dict(word_dict)
    for k, v in new_dict.items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    print(count_words('programming', ['python', 'java', 'javascript']))

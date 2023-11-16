#!/usr/bin/python3
""" module to test reddit api"""
from requests.auth import HTTPBasicAuth
from requests import post


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
    print(get_token())
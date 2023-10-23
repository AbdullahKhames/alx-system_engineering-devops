#!/usr/bin/python3
"""module to connect to api with requests package"""

import csv
from requests import get
from sys import argv


def connect():
    """connect function to call the api"""
    base_url = 'https://jsonplaceholder.typicode.com'
    todo = '/todos'
    users = '/users'
    emp_id = argv[1]
    todo_full_url = f'{base_url}{users}/{emp_id}{todo}'
    users_full_url = f'{base_url}{users}/{emp_id}'
    todos_resp = get(todo_full_url)
    users_resp = get(users_full_url)
    todos = todos_resp.json()
    user_data = users_resp.json()
    username = user_data.get('username')
    USER_ID = user_data.get('id')
    with open(f'{USER_ID}.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            status = todo.get('completed')
            name = todo.get('title')
            data = [f'{USER_ID}', f'{username}', f'{status}', f'{name}']
            writer.writerow(data)


if __name__ == "__main__":
    """prevents module from running when imported"""
    connect()

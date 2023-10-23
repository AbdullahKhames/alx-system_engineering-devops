#!/usr/bin/python3
"""module to connect to api with requests package"""

from json import dump
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
    data = {f"{USER_ID}": []}
    with open(f'{USER_ID}.json', 'w', encoding='UTF8') as f:
        for todo in todos:
            status = todo.get('completed')
            name = todo.get('title')
            data.get(f'{USER_ID}') \
                .append({"task": f"{name}",
                         "completed": status,
                         "username": f"{username}"})
        dump(data, f)


if __name__ == "__main__":
    """prevents module from running when imported"""
    connect()

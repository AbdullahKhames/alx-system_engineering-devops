#!/usr/bin/python3
"""module to connect to api with requests package"""

from json import dump
from requests import get


def connect():
    """connect function to call the api"""
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = '/todos'
    users = '/users'
    data = {}
    for i in range(1, 11):
        todo_full_url = f'{base_url}{users}/{i}{todo_url}'
        users_full_url = f'{base_url}{users}/{i}'
        todos_resp = get(todo_full_url)
        users_resp = get(users_full_url)
        todos = todos_resp.json()
        user_data = users_resp.json()
        username = user_data.get('username')
        ls = []
        for todo in todos:
            status = todo.get('completed')
            name = todo.get('title')
            ls.append({"username": f"{username}",
                       "task": f"{name}",
                       "completed": status,
                       })
        curr_dict = {f"{i}": ls}
        data.update(curr_dict)

    with open(f'todo_all_employees.json', 'w', encoding='UTF8') as f:
        dump(data, f)


if __name__ == "__main__":
    """prevents module from running when imported"""
    connect()

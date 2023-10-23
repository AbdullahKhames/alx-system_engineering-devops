#!/usr/bin/python3
"""module to connect to api with requests package"""
from requests import get
from sys import argv


def connect():
    base_url = 'https://jsonplaceholder.typicode.com'
    todo = '/todos'
    users = '/users'
    emp_id = argv[1]
    todo_full_url = f'{base_url}{users}/{emp_id}{todo}'
    users_full_url = f'{base_url}{users}/{emp_id}'
    todos_resp = get(todo_full_url)
    users_resp = get(users_full_url)
    todos = todos_resp.json()
    completed_todos = [todo for todo in todos if todo['completed'] is True]
    NUMBER_OF_DONE_TASKS = len(completed_todos)
    TOTAL_NUMBER_OF_TASKS = len(todos)
    user_data = users_resp.json()
    EMPLOYEE_NAME = user_data.get('name')
    emp_data = f'Employee {EMPLOYEE_NAME} is done \
with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'
    print(emp_data)
    for todo in completed_todos:
        task_name = todo.get('title')
        print(f'\t {task_name}')


if __name__ == "__main__":
    connect()

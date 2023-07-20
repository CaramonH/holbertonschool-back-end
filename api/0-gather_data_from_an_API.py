#!/usr/bin/python3
"""
API set up to retrieve data from a url
"""
import requests
import sys

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    id = sys.argv[1]
    request = requests.get('{}/users/{}/todos'.format(
        API_URL, id), params={"_expand": "user"})

    response = request.json()

    completed_tasks = [task for task in response if task['completed']]
    EMPLOYEE_NAME = response[0]['user']['name']
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(response)

    # Using custom placeholders for indentation
    INDENT = "    "  # 4 spaces for each level of indentation

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))

    for task in completed_tasks:
        print("{}{}".format(INDENT, task['title']))

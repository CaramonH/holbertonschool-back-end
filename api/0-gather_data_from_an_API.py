#!/usr/bin/python3
"""
API set up to retrieve data from a url
"""
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}{employee_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        employee_name = data["name"]
        done_tasks = data["completed_tasks"]
        total_tasks = data["total_tasks"]
        completed_task_titles = [task["title"] for task in data["tasks"] if task["completed"]]

        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in completed_task_titles:
            print("\t" + title)

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data from the API. {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

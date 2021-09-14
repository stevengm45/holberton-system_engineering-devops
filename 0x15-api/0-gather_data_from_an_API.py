#!/usr/bin/python3
""" This script use rest api return information about the id passed as argument """

if __name__ == "__main__":
    import requests
    from sys import argv
    html = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    employee_name = html['name']
    html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    tasks_no_completed = 0
    title_of_tasks = []

    for i in html:
        if i['userId'] == int(argv[1]):
            if i['completed']:
                title_of_tasks.append(i['title'])
            else:
                tasks_no_completed += 1

    print("Employee {} is done with tasks({}/{}):\n\t {}".format(
        employee_name, len(title_of_tasks),
        tasks_no_completed + len(title_of_tasks), "\n\t ".join(
            title_of_tasks)))

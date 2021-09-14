#!/usr/bin/python3
""" This script export data in the JSON format """
if __name__ == "__main__":
    import requests
    from sys import argv
    import json
    html = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    employee_name = html['username']
    html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    dic = {}
    dic[argv[1]] = []
    for item in html:
        if item['userId'] == int(argv[1]):
            tmp = {}
            tmp['task'] = item['title']
            tmp['completed'] = item['completed']
            tmp['username'] = employee_name
            dic[argv[1]].append(tmp)
    with open(argv[1] + ".json", "w+") as file:
        json.dump(dic, file)

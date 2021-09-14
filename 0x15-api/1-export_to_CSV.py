#!/usr/bin/python3
""" This scritp export data in the CSV format"""

if __name__ == "__main__":
    import requests
    from sys import argv
    html = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    employee_name = html['username']
    html = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    csv = ""
    for i in html:
        if i['userId'] == int(argv[1]):
            csv += '"{}","{}","{}","{}"\n'.format(
                i['userId'], employee_name, i['completed'], i['title'])

    with open(argv[1] + ".csv", "w+") as file:
        file.write(csv)

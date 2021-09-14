#!/usr/bin/python3
""" with rest api return information about the id passed as argument """
if __name__ == "__main__":
    import requests
    import json
    jsonf = {}
    json_dict = {}
    dicl = []
    html = "https://jsonplaceholder.typicode.com/"
    json_usr = requests.get("{}users".format(html)).json()
    json_tds = requests.get("{}todos".format(html)).json()
    for usr in json_usr:
        for dic in json_tds:
            if dic['userId'] == usr['id']:
                json_dict['task'] = dic['title']
                json_dict['completed'] = dic['completed']
                json_dict['username'] = usr['username']
                dicl.append(json_dict)
                json_dict = {}
        jsonf[usr['id']] = dicl
        dicl = []
    with open("todo_all_employees.json", "w+") as file:
        json.dump(jsonf, file)

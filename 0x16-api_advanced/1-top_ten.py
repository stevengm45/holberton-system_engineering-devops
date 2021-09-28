#!/usr/bin/python3
''' Using Reddit api to get the top 10 posts on a subreddit '''
from requests import get


def top_ten(subreddit):
    ''' Prints the top posts titles or prints None '''
    html = get("https://www.reddit.com/r/{}/hot.json?limit=10".
               format(subreddit),
               headers={"User-Agent": "Custom_user"},
               allow_redirects=False)

    if html.status_code == 200:
        for child in html.json()['data']['children']:
            print(child['data']['title'])
    else:
        print(None)

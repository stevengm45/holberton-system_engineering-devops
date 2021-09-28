#!/usr/bin/python3
''' Using Reddit api to get the top 10 posts on a subreddit '''
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    ''' Return list of all subreddit posts or None '''
    html = get("https://www.reddit.com/r/{}/hot.json?after={}".
               format(subreddit, after),
               headers={"User-Agent": "Custom_user"},
               allow_redirects=False)
    if html.status_code != 200:
        return None

    data = html.json().get('data')
    children = data['children']
    for i in children:
        hot_list.append(i.get('data')['title'])
    after = data['after']
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list

#!/usr/bin/python3
"""get the first 10 info from reddit api"""


def top_ten(subreddit):
    """first 10"""
    import requests

    web = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla"},
                       allow_redirects=False)

    if web.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in web.json().get("data").get("children")]

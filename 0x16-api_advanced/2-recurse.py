#!/usr/bin/python3
"""get info using recursion"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    import requests

    web = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       params={"count": count, "after": after},
                       headers={"User-Agent": "mozilla"},
                       allow_redirects=False)
    if web.status_code >= 400:
        return None

    h_list = hot_list + [child.get("data").get("title")
                         for child in web.json()
                         .get("data")
                         .get("children")]

    info = web.json()
    if not info.get("data").get("after"):
        return h_list

    return recurse(subreddit, h_list, info.get("data").get("count"),
                   info.get("data").get("after"))

#!/usr/bin/python3
"""get info from reddit api"""


def number_of_subscribers(subreddit):
    import requests

    web = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla",
                                "Content-Type": "application/json"},
                       allow_redirects=False,)
    if web.status_code >= 300:
        return 0

    return web.json().get("data").get("subscribers")

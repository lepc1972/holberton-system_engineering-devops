#!/usr/bin/python3
"""get the first 10 info from reddit api"""


def top_ten(subreddit):
    import requests

    web = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla",
                                "Content-Type": "application/json"},
                       allow_redirects=False,)

    if web.status_code >= 300:
        return 0
    [print(child.get("data").get("title"))
     for child in web.json().get("data").get("children")]

#!/usr/bin/python3
""" Module for Reddit API"""


def number_of_subscribers(subreddit):
    """ Function returns total count of subscribers """
    import requests
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'RedditUserAgent/1.0'}

    try:
        response = requests.get(
           base_url,
           headers=headers,
           allow_redirects=False
        )

        if response.status_code >= 300:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except requests.exceptions.RequestException:
        return 0

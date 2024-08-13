#!/usr/bin/python3
"""Module that retrieves data from reddit API"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function that retrieves top ten data"""
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'RedditUserAgent/1.0(by u/Pelo101Alx)'}

    try:

        response = requests.get(
            base_url,
            headers=headers,
            allow_redirects=False

        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print(None)
            return

        for post in children[:10]:
            print(post['data']['title'])

    except requests.exceptions.RequestException:
        print(None)

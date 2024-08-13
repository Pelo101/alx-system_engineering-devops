#!/usr/bin/python3
"""Module that retrieves data from reddit API"""
import requests


def top_ten(subreddit):
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

        data = response.json().get('data', {}).get('children', [])
        if not data:
            print(None)
            return

        for post in data:
            print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException:
        print(None)

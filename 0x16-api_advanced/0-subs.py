#!/usr/bin/python3
""" Module for Reddit API"""


def number_of_subscribers(subreddit):
    """ Function returns total count of subscribers """
    import requests
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditUserAgent'}

    try:
        response = requests.get(
           base_url,
           headers=headers,
           allow_redirects=False
        )

        if response.status_code >= 300:
            return 0

        data = response.json()
        return data.get('data').get('subscribers')

    except requests.exceptions.RequestException:
        return 0

#!/usr/bin/python3
"""
sends a request to the URL passed as an arrgument and
displays the value of the variable X-Request-Id in the
response header using requests package
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
    displays the value of the variable X-Request-Id in the response header

- Am using the packages urllib and sys
- Am not allowed to import packages other than urllib and sys
- The value of this variable is different for each request
- Am not checking arguments passed to the script (number or type)
"""


import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    rqst = requests.get(url)
    print(rqst.headers.get('X-Request-Id')

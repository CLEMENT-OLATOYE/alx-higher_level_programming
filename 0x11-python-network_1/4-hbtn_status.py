#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = request.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

import requests


def make_request(address):
    requests.get(address)
    return True


def parse_response():
    res = make_request("google.com")
    if res:
        return "Successful request"
    else:
        return "Error in request"

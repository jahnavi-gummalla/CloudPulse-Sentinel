import requests

def get_request(url, headers=None):
    return requests.get(url, headers=headers)

def post_request(url, payload, headers=None):
    return requests.post(url, json=payload, headers=headers)

def put_request(url, payload, headers=None):
    return requests.put(url, json=payload, headers=headers)

def delete_request(url, headers=None):
    return requests.delete(url, headers=headers)
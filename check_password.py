import requests 
import sys
import hashlib

# This function requests our data and gives us a response
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def read_res(response):
    print(response.text)

def pwned_api_heck(password):
    sha1_password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first_5_chars, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first_5_chars)
    print(first_5_chars, tail)
    return read_res(response)

if __name__ == '__main__':
    pwned_api_heck('123')
    
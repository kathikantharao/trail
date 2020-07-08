import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError (f"Error fetchin: {res.status_code}, check the api and try again")
    return res

def get_password_leak(hashes, hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashes_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1hashing = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
    first, tail = sha1hashing[:5], sha1hashing[5:]
    response = request_api_data(first)
    return get_password_leak(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times, you should probabily change the password")
        else:
            print(f"{password} was not found, You may use the password")
    return 'Done'


if __name__ == '__main__':
    a = sys.argv[1:]
    print(main(a))


# python3 passcheck.py
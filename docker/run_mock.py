import requests

user = {}
user['email'] = 'string'
user['password'] = 'string'
user['firstname'] = 'string'
user['lastname'] = 'string'
user['admin'] = True

room = {'token': 'blaaa', 'roomId': 1, 'categoryId': '2'}

r = requests.get('http://127.0.0.1:4000/catalog')
if r.status_code == 200:
    print("/catalog OK")
else:
    print("/catalog fail")
    exit(1)

r = requests.post('http://127.0.0.1:5000/price', json=room)
if r.status_code == 200:
    print("/price OK")
else:
    print("/price fail")
    exit(1)

r = requests.post('http://127.0.0.1:3000/register_user', json=user)
if r.status_code == 200:
    print("/register_user OK")
else:
    print("/register_user fail")
    exit(1)
    
r = requests.post('http://127.0.0.1:3000/login_user', json=user)
if r.status_code == 200:
    print("/login_user OK")
else:
    print("/login_user fail")
    exit(1)

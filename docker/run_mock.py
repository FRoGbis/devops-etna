import requests

user = {}
user['email'] = 'string'
user['password'] = 'string'
user['firstname'] = 'string'
user['lastname'] = 'string'
user['admin'] = True

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

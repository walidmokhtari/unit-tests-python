import requests, json

res = requests.post('http://127.0.0.1:5000/register',
                    json={'firstName': 'Alex', 'lastName': 'LIMA', 'age': 29}).status_code
if res == 200:
    print("TEST IS OK")
else:
    print("ERROR: unexpected value")

Get = requests.get('http://127.0.0.1:5000/').status_code
if Get == 200:
    print("TEST IS OK")
else:
    print("ERROR: unexpected value")


res = requests.get('http://127.0.0.1:5000/user/Walid')
if res.json()['age'] == 23:
    print("TEST IS OK")
else:
    print("ERROR: unexpected value")


res = requests.put('http://127.0.0.1:5000/update-user/Walid',
                    json={'firstName': 'Walid Modified', 'lastName': 'MOKHTARI Modified', 'age': 24}).status_code
if res == 200:
    print("TEST IS OK")
else:
    print("ERROR: unexpected value")


res = requests.get('http://127.0.0.1:5000/')
print(res.json())
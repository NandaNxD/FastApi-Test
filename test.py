import requests

file = {'file': open('in.jpg', 'rb')}

def req():
    response=requests.get('http://127.0.0.1:8000/')
    print(response.json()) 

req()
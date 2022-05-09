from importlib.resources import path
from fastapi import Body
import requests

file = {'file': open('dx.jpg', 'rb')}

def req():
    response=requests.post('http://127.0.0.1:8000/handle-file',files=file)
    print(response.json()) 

req()
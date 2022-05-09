import requests

file = {'file': open('in.jpg', 'rb')}

def req():
    response=requests.post('https://park11.herokuapp.com/',files=file)
    print(response.json()) 

req()
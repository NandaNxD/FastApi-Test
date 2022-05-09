import requests

file = {'file': open('in.jpg', 'rb')}

def req():
    response=requests.post('https://eb2f-117-213-242-137.in.ngrok.io/handle-file',files=file)
    print(response.json()) 

req()
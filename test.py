import requests
file = {'file': open('image3.jpg', 'rb')}

def req():
    response=requests.post('https://smartparkingapi1.herokuapp.com/',files=file)
    #response=requests.post('https://smartparkingsystem1.herokuapp.com/',files=file)
    #response=requests.post('http://localhost:8000/',files=file)
    if not response.ok:
        print('request failed')
        print(response.status_code)
    else:
        if(response.json()==None):
            print('Object is not a Car')
        else:
            print(response.json()) 

req()
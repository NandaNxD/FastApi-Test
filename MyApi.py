from traceback import print_exc
from fastapi import FastAPI
import requests
from fastapi import FastAPI, File
from Main import getLicensePlateNumber

app=FastAPI()


@app.get('/')
def inx():
    return "Api Working"


@app.post('/')
async def handle_file(file:bytes=File(...)):
    f=open('image.jpg','wb')
    f.write(file)
    f.close()
    #r=open('image.jpg')
    result=getLicensePlateNumber('image.jpg')
    #r.close()
    return result
    
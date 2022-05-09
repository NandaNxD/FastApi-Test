from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, File, UploadFile

app=FastAPI()

def getLicensePlateNumber(file):
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=file),
            headers={'Authorization': 'Token f52c6f2941e5bc78ad0ec88f04080a579f7b4509'})
        reg = response.json()['results'][0]['plate']
        return reg

@app.post('/handle-file')
async def handle_file(file:bytes=File(...)):
    f=open('image.jpg','wb')
    f.write(file)
    f.close()
    r=open('image.jpg','rb')
    result=getLicensePlateNumber(r)
    r.close()
    return result
    
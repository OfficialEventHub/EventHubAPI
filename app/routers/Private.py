from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

Private = APIRouter()
load_dotenv()

def private_key_check(auth_header):
    print(os.environ["PRIVATE_KEY"])
    if auth_header == os.environ["PRIVATE_KEY"]:
        return True
    else:
        return False

def invalid_key():
    return JSONResponse({
        "success": 0,
        "data": {
            "message": "Invalid authorization header!"
        }
    },status_code=401)


@Private.get('/test')
def test(request: Request):
    auth_header = request.headers.get('Authorization')
    if private_key_check(auth_header) == True:
        return JSONResponse({
            "success": 1,
            "data": {
                "message": "Valid authorization header!"
            }
        })
    else:
        return invalid_key()


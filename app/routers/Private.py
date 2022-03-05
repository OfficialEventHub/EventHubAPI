from fastapi import APIRouter
Private = APIRouter()


@Private.get('/test')
def test():
    return 'Hello World!'


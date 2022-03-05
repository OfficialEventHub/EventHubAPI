from fastapi import FastAPI
from .routers.Private import Private
from .routers.Public import Public

app = FastAPI()

app.include_router(Private,prefix='/private')
app.include_router(Public,prefix='/public')
    
@app.get('/')
def hello():
    return 'Hello World!'
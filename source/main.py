from fastapi import FastAPI

from source import settings
from source import routes


app = FastAPI()

routes.register(app)

@app.on_event('startup')
async def startup():
    pass

@app.on_event('shutdown')
async def shutdown():
    pass

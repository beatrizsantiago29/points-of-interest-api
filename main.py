from fastapi import FastAPI

app = FastAPI() # criacao do app

from poi_routes import poi_router
app.include_router(poi_router)
from fastapi import FastAPI
from core.config import settings
from db.base import BaseModel  
from db.session import engine   
from route.index import datefact
from core.middleware import RequestHandlingMiddleware

def routeConfig(app):
	app.include_router(datefact)

def addMiddleware(app):
  app.add_middleware(RequestHandlingMiddleware)

def syncTable():           
	BaseModel.metadata.create_all(bind=engine)
	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	addMiddleware(app)
	routeConfig(app)
	syncTable()       
	return app

app = start_application()

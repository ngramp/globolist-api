from fastapi import FastAPI
from app.routers import authentication_router, users_router, articles_router

app = FastAPI()

# Include the routers
app.include_router(authentication_router)
app.include_router(users_router)
app.include_router(articles_router)

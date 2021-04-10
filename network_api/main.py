from fastapi import FastAPI

from network_api.routers import commands

app = FastAPI()

app.include_router(
    commands.router,
    prefix="/api",
    tags=["commands"],
)

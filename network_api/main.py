from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import ios

app = FastAPI()

app.include_router(ios.router)
app.include_router(
    ios.router, prefix="/api/cisco/ios", tags=["ios"],
)

from fastapi import FastAPI
from .ris_integration import ris_integration_router
from .config import token_initialization

app = FastAPI()

app.include_router(
    ris_integration_router
)


@app.on_event("startup")
async def startup_event():
    await token_initialization()

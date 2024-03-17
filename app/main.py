from fastapi import FastAPI
from .services.route import internal_req
import os

llama_internal_endpoint = os.getenv("INTERNAL_API_ENDPOINT")

app = FastAPI()
app.include_router(internal_req)

@app.get("/")
async def root():
    return { "message": "Llama Public Service" }

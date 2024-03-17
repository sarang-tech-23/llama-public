from dotenv import load_dotenv
import socket
from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os

load_dotenv()

internal_req = APIRouter()
llama_internal_endpoint = os.getenv("INTERNAL_API_ENDPOINT")
# print('outside_postCall_internal_api-------> ', llama_internal_endpoint)

class Question(BaseModel):
    question: str
   
@internal_req.post("/gpt", tags=["Llama"])
async def llama(payload: Question):
    global llama_internal_endpoint
    print('inside_postCall_internal_api-------> ', llama_internal_endpoint)
    demo_res = requests.get('https://pokeapi.co/api/v2')
    response=None
    

    # Get the hostname of the machine
    hostname = socket.gethostname()

    # Print the hostname
    print("Hostname:", hostname)
    try: 
        response = requests.post(llama_internal_endpoint, json={"question": payload.question})
        return f'Answer of this question is this: {response.json()}'
    except Exception as e:
        # return f"Geting error {e} \n\n demo response: {demo_res.json()}"
        return {
            "error": e,
            "error_message": f'{e}',
            "demo_res": demo_res.json(),
        }
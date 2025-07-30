from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

import random

load_dotenv()

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def health_check() -> dict:
    """
    Function to check health check of endpoint

    Args: 
    
        None

    Returns:

        response: dict = A response for the health check of the 
        api.
    """
    response: dict = {"message": "Profanity Checker is running"}
    return response

@app.get("/random")
async def get_random() -> dict:
    """
    Get random function returns a random
    integer, use this for testing.

    Args: 
        
        None

    Returns:

        response: dict = A response with the random
        integer.
    """
    random_integer = random.randint(1, 100)

    response: dict = {"integer": f"{random_integer}"}

    return response

@app.get("/multiply/{number}")
async def multiply(number: int) -> dict:
    """
    Based on the random function
    multiplies a number time the number amount.

    Args:

        number: int = An integer number

    Returns:

        response: dict = A response with the 
        calculation
    """
    random_integer: int = random.randint(1, 100)

    total: int = number * random_integer

    response: dict = {"total": f"{total}"}

    return response



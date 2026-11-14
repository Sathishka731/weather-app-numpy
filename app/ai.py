import asyncio
from google import genai
from app.config import settings


client = genai.Client(api_key=settings.API_KEY)

async def call_model(message:str)-> str:

    response = await client.aio.models.generate_content(
        model=settings.API_MODEL,
        contents=message
    )

    return response.text


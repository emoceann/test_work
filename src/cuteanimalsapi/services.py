import httpx
import tempfile


async def get_cute_animal():
    url = 'http://placekitten.com/200/300'
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        return response.content

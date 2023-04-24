import httpx
from settings import settings


async def get_dict_currencies():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://api.apilayer.com/exchangerates_data/symbols",
            headers={"apikey": settings.EXCHANGE_RATES_API_KEY}
        )
        return response.json()


async def get_exchange_rates(cur1: int, cur2: int, amount: float):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur2}&from={cur1}&amount={amount}"
    headers = {"apikey": settings.EXCHANGE_RATES_API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=headers)
    return response.json()

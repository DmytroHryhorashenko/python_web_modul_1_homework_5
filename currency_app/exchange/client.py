import aiohttp
import asyncio

class PrivatBankClient:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="

    async def fetch_rates(self, date: str) -> dict:
        url = self.BASE_URL + date
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response:
                    if response.status != 200:
                        raise Exception(f"HTTP error: {response.status}")
                    return await response.json()
        except asyncio.TimeoutError:
            raise Exception("Request timeout")
        except aiohttp.ClientError as e:
            raise Exception(f"Network error: {e}")
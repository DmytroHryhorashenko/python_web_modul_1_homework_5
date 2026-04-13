import asyncio
import websockets
import json

from exchange.client import PrivatBankClient
from exchange.service import ExchangeService
from exchange.logger import log_command

client = PrivatBankClient()
service = ExchangeService(client)


def format_data(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


async def handler(websocket):
    print("🔥 CLIENT CONNECTED")

    await websocket.send("👋 Welcome! Use: exchange <days 1-10> [USD EUR GBP]")

    async for message in websocket:
        message = message.strip()
        print("📩 RECEIVED:", message)

        if not message.startswith("exchange"):
            await websocket.send("❌ Use: exchange 2 USD EUR")
            continue

        parts = message.split()

        try:
            days = int(parts[1]) if len(parts) > 1 else 1
        except:
            await websocket.send("❌ Days must be number")
            continue

        currencies = parts[2:] if len(parts) > 2 else ["USD", "EUR"]

        if days < 1 or days > 10:
            await websocket.send("❌ Only 1–10 days allowed")
            continue

        data = await service.get_last_days_rates(days, currencies)

        await log_command(message)

        await websocket.send(format_data(data))


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("🚀 Server running ws://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
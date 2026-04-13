import asyncio
import websockets
from exchange.client import PrivatBankClient
from exchange.service import ExchangeService
from exchange.logger import log_command

client = PrivatBankClient()
service = ExchangeService(client)

async def handler(websocket):
    await websocket.send("Введите: exchange 2 USD EUR")

    async for message in websocket:
        try:
            if message.startswith("exchange"):
                parts = message.split()
                days = int(parts[1]) if len(parts) > 1 else 1
                currencies = parts[2:] if len(parts) > 2 else ["USD", "EUR"]

                data = await service.get_last_days_rates(days, currencies)

                await websocket.send(str(data))

                await log_command(message)

            else:
                await websocket.send("Unknown command")

        except Exception as e:
            await websocket.send(f"Ошибка: {e}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("✅ WebSocket server started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
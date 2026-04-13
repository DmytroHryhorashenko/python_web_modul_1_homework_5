import asyncio
import sys
from exchange.client import PrivatBankClient
from exchange.service import ExchangeService

async def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    currencies = sys.argv[2:] if len(sys.argv) > 2 else ["USD", "EUR"]

    client = PrivatBankClient()
    service = ExchangeService(client)

    data = await service.get_last_days_rates(days, currencies)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
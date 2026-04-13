from datetime import datetime, timedelta
from .models import CurrencyRate, DailyRate

class ExchangeService:
    def __init__(self, client):
        self.client = client

    async def get_last_days_rates(self, days: int, currencies=("USD", "EUR")):
        if days < 1 or days > 10:
            raise ValueError("Days must be between 1 and 10")

        result = []

        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime("%d.%m.%Y")
            data = await self.client.fetch_rates(date)

            rates = {}
            for item in data.get("exchangeRate", []):
                if item.get("currency") in currencies:
                    rates[item["currency"]] = CurrencyRate(
                        purchase=item.get("purchaseRate", 0.0),
                        sale=item.get("saleRate", 0.0)
                    )

            result.append({
                date: {
                    cur: {
                        "purchase": val.purchase,
                        "sale": val.sale
                    } for cur, val in rates.items()
                }
            })

        return result
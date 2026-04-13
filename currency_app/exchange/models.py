from dataclasses import dataclass

@dataclass
class CurrencyRate:
    purchase: float
    sale: float

@dataclass
class DailyRate:
    date: str
    rates: dict
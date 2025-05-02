class SpyExchangeRateGw:
    def __init__(self):
        self.called = 0

    def get_exchange_rate(self, year:int, month:int, day:int) -> dict:
        self.called += 1
        return {
            "date": "2025-04-25",
            "ticker": "JPY=X",
            "price": 142.87
        }

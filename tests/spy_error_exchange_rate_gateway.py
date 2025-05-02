import datetime


class SpyErrorExchangeRateGw:
    def __init__(self):
        self.called = 0
        self.requested_dates = []

    def get_exchange_rate(self, year:int, month:int, day:int) -> dict:
        self.called += 1
        date_str = datetime.date(year, month, day).strftime("%Y-%m-%d")
        self.requested_dates.append(date_str)
        raise ValueError()

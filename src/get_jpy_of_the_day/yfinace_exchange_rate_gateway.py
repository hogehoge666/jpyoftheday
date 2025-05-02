import yfinance as yf
import datetime
import math

PRICE_TYPE_CLOSE = "Close"
DATE_FORMAT = "%Y-%m-%d"
JPY_X = "JPY=X"


class YfinaceExchangeRateGw:
    def get_exchange_rate(self, year:int, month:int, day:int) -> dict:
        start_date = datetime.date(year, month, day)
        end_date = start_date + datetime.timedelta(days=1)
        start_date_str = start_date.strftime(DATE_FORMAT)
        end_date_str = end_date.strftime(DATE_FORMAT)
        response = yf.download(JPY_X, start=start_date_str, end=end_date_str, interval="1d", progress=False)
        try:
            closing_price_raw = response.at[start_date_str, (PRICE_TYPE_CLOSE, JPY_X)]
        except KeyError:
            raise ValueError("Price data not found for the requested date")
        closing_price = math.floor(closing_price_raw * 100) / 100
        return {
            "date": start_date_str,
            "ticker": JPY_X,
            "price": closing_price
        }

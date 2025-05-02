import datetime

from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_output_data import OutputData

from logging import getLogger, StreamHandler, DEBUG, INFO
logger = getLogger(__name__)
handler = StreamHandler()
logger.setLevel(INFO)
logger.addHandler(handler)


class GetJpyOfTheDayUsecase:
    def __init__(self, exchange_rate_gateway, retry_limit=5):
        self.gateway = exchange_rate_gateway
        self.retry_limit = retry_limit

    def _is_weekday(self, year:int, month:int, day:int) -> bool:
        date = datetime.date(year, month, day)
        if date.weekday() in (5, 6):
            return False
        return True

    def _is_new_year(self, year:int, month:int, day:int) -> bool:
        if month == 1 & day == 1:
            return True
        return False

    def _is_future(self, year:int, month:int, day:int) -> bool:
        today_date = datetime.datetime.now().date()
        target_date = datetime.date(year, month, day)
        return today_date < target_date

    def ensure_market_is_open(self, year, month, day):
        if not self._is_weekday(year, month, day):
            raise ValueError("Requested date is weekend.  Market is closed.")
        if self._is_new_year(year, month, day):
            raise ValueError("Requested date is holiday.  Market is closed.")
        if self._is_future(year, month, day):
            raise RuntimeError("Requested date is future.  This request is invalid.")

    def _get_price_from_gateway(self, input_data:InputData):
        year = input_data.year
        month = input_data.month
        day = input_data.day
        retry= 0
        while True:
            if retry >= self.retry_limit:
                raise RuntimeError("Retry limit is exceeded.  Try with other date.")
            try:
                self.ensure_market_is_open(year, month, day)
                response = self.gateway.get_exchange_rate(year, month, day)
                return response
            except ValueError:
                retry += 1
                requested_date = datetime.date(year, month, day)
                new_date = requested_date + datetime.timedelta(days=1)
                year = new_date.year
                month = new_date.month
                day = new_date.day
                logger.debug(f"Retrying {retry}")

    def get_price_of_the_day(self, input_data:InputData, presenter) -> dict:
        response = self._get_price_from_gateway(input_data)
        output_data = OutputData(
            ticker=response["ticker"],
            requested_date=datetime.date(input_data.year, input_data.month, input_data.day),
            retrieved_date=datetime.datetime.strptime(response["date"], "%Y-%m-%d"),
            price=response["price"],
        )
        presenter.present(output_data)

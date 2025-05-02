import datetime

from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_output_data import OutputData


class SpyGetJpyOfTheDayUsecase:
    def __init__(self, exchange_rate_gateway, retry_limit=5):
        self.gateway = exchange_rate_gateway
        self.retry_limit = retry_limit
        self.called = 0

    def get_price_of_the_day(self, input_data:InputData, presenter) -> dict:
        self.called += 1
        output_data = OutputData(
            ticker="JPY=X",
            retrieved_date=datetime.date(2025, 4, 25),
            requested_date=None,
            price=142.87,
        )
        presenter.present(output_data)
        return {}

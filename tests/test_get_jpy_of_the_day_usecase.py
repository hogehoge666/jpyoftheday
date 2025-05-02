import unittest
import datetime

from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_usecase import GetJpyOfTheDayUsecase
from spy_error_exchange_rate_gateway import SpyErrorExchangeRateGw
from spy_exchange_rate_gateway import SpyExchangeRateGw
from spy_get_jpy_of_the_day_presenter import SpyGetJpyOfTheDayPresenter


class UseCaseTestCase(unittest.TestCase):
    def setUp(self):
        self.spy_gw = SpyExchangeRateGw()
        self.usecase = GetJpyOfTheDayUsecase(self.spy_gw)

    def test_given_weekend_raises_valueerror(self):
        # Saturday
        with self.assertRaises(ValueError):
            self.usecase.ensure_market_is_open(2025, 4, 26)
        # Sunday
        with self.assertRaises(ValueError):
            self.usecase.ensure_market_is_open(2025, 4, 27)

    def test_given_new_year_raise_valueerror(self):
        with self.assertRaises(ValueError):
            self.usecase.ensure_market_is_open(2025, 1, 1)

    def test_given_future_date_raise_valueerror(self):
        future_datetime = datetime.datetime.now() + datetime.timedelta(days=1)
        future_date = future_datetime.date()
        if future_date.weekday() >= 5:
            future_date += datetime.timedelta(days=2)
        with self.assertRaises(RuntimeError):
            self.usecase.ensure_market_is_open(future_date.year, future_date.month, future_date.day)

    def test_given_weekday_call_exchange_rate_gateway(self):
        input_data = InputData(2025, 4, 25)
        spy_presenter = SpyGetJpyOfTheDayPresenter()
        self.usecase.get_price_of_the_day(input_data, spy_presenter)
        self.assertEqual(1, self.spy_gw.called)
        self.assertEqual(1, spy_presenter.present_called)
        output_data = spy_presenter.output_data
        self.assertEqual("JPY=X", output_data.ticker)
        self.assertEqual(142.87, output_data.price)
        self.assertEqual("2025-04-25", output_data.requested_date.strftime("%Y-%m-%d"))
        self.assertEqual("2025-04-25", output_data.retrieved_date.strftime("%Y-%m-%d"))

    def test_when_retry_limit_reached_raise_runtimeerror(self):
        retry_limit = 3
        error_spy_gw = SpyErrorExchangeRateGw()
        usecase = GetJpyOfTheDayUsecase(error_spy_gw, retry_limit)
        input_data = InputData(2025, 4, 21)
        spy_presenter = SpyGetJpyOfTheDayPresenter()
        with self.assertRaises(RuntimeError):
            usecase.get_price_of_the_day(input_data, spy_presenter)
        self.assertEqual(retry_limit, error_spy_gw.called)
        self.assertListEqual(
            ["2025-04-21", "2025-04-22", "2025-04-23"],
            error_spy_gw.requested_dates
        )
        self.assertEqual(0, spy_presenter.present_called)
        self.assertIsNone(spy_presenter.output_data)


if __name__ == '__main__':
    unittest.main()

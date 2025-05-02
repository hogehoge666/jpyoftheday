import unittest

from get_jpy_of_the_day.yfinace_exchange_rate_gateway import YfinaceExchangeRateGw

@unittest.skip("Skipping tests against real API")
class ExchangeRateGatewayTestCase(unittest.TestCase):
    def test_get_jpyd_exchange_rate(self):
        gw = YfinaceExchangeRateGw()
        response = gw.get_exchange_rate(year=2025, month=4, day=25)
        self.assertEqual(142.87, response["price"])

    def test_given_weekend_requested_return_valueerror(self):
        gw = YfinaceExchangeRateGw()
        with self.assertRaises(ValueError):
            gw.get_exchange_rate(year=2025, month=4, day=26)

    def test_given_holiday_requested_return_valueerror(self):
        gw = YfinaceExchangeRateGw()
        with self.assertRaises(ValueError):
            gw.get_exchange_rate(year=2025, month=1, day=1)



if __name__ == '__main__':
    unittest.main()

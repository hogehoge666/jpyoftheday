import unittest

from get_jpy_of_the_day.get_jpy_of_the_day_controller import GetJpyOfTheDayController
from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from spy_get_jpy_of_the_day_usecase import SpyGetJpyOfTheDayUsecase
from spy_get_jpy_of_the_day_viewimpl import SpyGetJpyOfTheDayViewImpl
from spy_exchange_rate_gateway import SpyExchangeRateGw
from spy_get_jpy_of_the_day_presenter import SpyGetJpyOfTheDayPresenter


class ControllerTestCase(unittest.TestCase):
    def test_usecase_and_presenter_and_view_are_called(self):
        spy_gw = SpyExchangeRateGw()
        spy_usecase = SpyGetJpyOfTheDayUsecase(spy_gw)
        spy_presenter = SpyGetJpyOfTheDayPresenter()
        spy_view = SpyGetJpyOfTheDayViewImpl()
        controller = GetJpyOfTheDayController(spy_usecase, spy_presenter, spy_view)
        input_data = InputData(2025, 4, 25)
        controller.handle(input_data)
        self.assertEqual(1, spy_usecase.called)
        self.assertEqual(1, spy_presenter.present_called)
        self.assertEqual(1, spy_presenter.get_view_model_called)
        self.assertEqual(1, spy_view.called)


if __name__ == '__main__':
    unittest.main()

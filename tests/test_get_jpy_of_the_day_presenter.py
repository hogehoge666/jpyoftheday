import unittest
import datetime

from get_jpy_of_the_day.get_jpy_of_the_day_output_data import OutputData
from get_jpy_of_the_day.get_jpy_of_the_day_presenter import GetJpyOfTheDayPresenter


class PresenterTestCase(unittest.TestCase):

    def test_view_model_built_from_output_data(self):
        date = datetime.date(2025, 4, 25)
        output_data = OutputData(
            ticker="JPY=X",
            requested_date=date,
            retrieved_date=date,
            price=142.87)
        presenter = GetJpyOfTheDayPresenter()
        presenter.present(output_data)
        view_model = presenter.get_view_model()
        self.assertDictEqual(
            {
                "ticker": "JPY=X",
                "requested_date": "2025-04-25",
                "requested_day_of_the_week": "Fri",
                "retrieved_date": "2025-04-25",
                "retrieved_day_of_the_week": "Fri",
                "price": 142.87
            },
            view_model
        )


if __name__ == '__main__':
    unittest.main()

from get_jpy_of_the_day.get_jpy_of_the_day_output_data import OutputData


class SpyGetJpyOfTheDayPresenter:

    def __init__(self):
        self.present_called = 0
        self.get_view_model_called = 0
        self.output_data = None

    def present(self, output_data:OutputData):
        self.present_called += 1
        self.output_data = output_data

    def get_view_model(self) -> dict:
        self.get_view_model_called += 1
        return {}

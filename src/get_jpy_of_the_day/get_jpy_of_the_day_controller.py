from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_presenter import GetJpyOfTheDayPresenter
from get_jpy_of_the_day.get_jpy_of_the_day_usecase import GetJpyOfTheDayUsecase
from get_jpy_of_the_day.get_jpy_of_the_day_viewimpl import GetJpyOfTheDayViewImpl


class GetJpyOfTheDayController:
    def __init__(
            self,
            usecase: GetJpyOfTheDayUsecase,
            presenter: GetJpyOfTheDayPresenter,
            view: GetJpyOfTheDayViewImpl):
        self.usecase = usecase
        self.presenter = presenter
        self.view = view

    def handle(self, input_data: InputData):
        self.usecase.get_price_of_the_day(input_data, self.presenter)
        view_model = self.presenter.get_view_model()
        self.view.generate_view(view_model)

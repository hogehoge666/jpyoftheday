from get_jpy_of_the_day.get_jpy_of_the_day_output_data import OutputData


class GetJpyOfTheDayPresenter:

    def __init__(self):
        self.view_model = {}

    def present(self, output_data:OutputData):
        days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        requested_day = output_data.requested_date.weekday()
        retrieved_day = output_data.retrieved_date.weekday()
        self.view_model = {
            "ticker": output_data.ticker,
            "price": output_data.price,
            "requested_date": output_data.requested_date.strftime("%Y-%m-%d"),
            "requested_day_of_the_week": days_of_the_week[requested_day],
            "retrieved_date": output_data.retrieved_date.strftime("%Y-%m-%d"),
            "retrieved_day_of_the_week": days_of_the_week[retrieved_day]
        }

    def get_view_model(self) -> dict:
        return self.view_model

import datetime


class OutputData:
    def __init__(
            self,
            ticker:str,
            retrieved_date:datetime.date,
            requested_date:datetime.date,
            price:float
    ):
        self.ticker = ticker
        self.retrieved_date = retrieved_date
        self.requested_date = requested_date
        self.price = price

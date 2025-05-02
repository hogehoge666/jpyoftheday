import datetime

from get_jpy_of_the_day.get_jpy_of_the_day_controller import GetJpyOfTheDayController
from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_presenter import GetJpyOfTheDayPresenter
from get_jpy_of_the_day.get_jpy_of_the_day_usecase import GetJpyOfTheDayUsecase
from get_jpy_of_the_day.get_jpy_of_the_day_viewimpl import GetJpyOfTheDayViewImpl
from get_jpy_of_the_day.yfinace_exchange_rate_gateway import YfinaceExchangeRateGw



gw = YfinaceExchangeRateGw()
usecase = GetJpyOfTheDayUsecase(gw)
presenter = GetJpyOfTheDayPresenter()
view = GetJpyOfTheDayViewImpl()

controller = GetJpyOfTheDayController(usecase, presenter, view)


print("")
print("##############################")
print("    USD to JPY converter")
print("##############################")
print("")
print("Type 'q' to exit")
while True:
    user_input = input("Input date(eg: 2025-04-26): ")
    if user_input == "q":
        print("")
        exit()
    if user_input == "":
        continue
    print("")

    input_data = None
    try:
        input_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")
    except ValueError as e:
        print("Input Error: Please specify date in correct format.")
        print(e)
        continue

    if input_date == None:
        print("Input Error: your input date seems invalid.  Please try again.")
        continue
    input_data = InputData(input_date.year, input_date.month, input_date.day)
    try:
        controller.handle(input_data)
    except RuntimeError as e:
        print("Runtime Error: something bad happened while processing your request.")
        print(e)

    print("")


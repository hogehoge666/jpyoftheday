import datetime
from socketserver import StreamRequestHandler

from get_jpy_of_the_day.get_jpy_of_the_day_controller import GetJpyOfTheDayController
from get_jpy_of_the_day.get_jpy_of_the_day_input_data import InputData
from get_jpy_of_the_day.get_jpy_of_the_day_presenter import GetJpyOfTheDayPresenter
from get_jpy_of_the_day.get_jpy_of_the_day_usecase import GetJpyOfTheDayUsecase
from get_jpy_of_the_day.get_jpy_of_the_day_viewimpl import GetJpyOfTheDayViewImpl
from get_jpy_of_the_day.yfinace_exchange_rate_gateway import YfinaceExchangeRateGw

from logging import getLogger, StreamHandler, DEBUG, INFO, Formatter

logger = getLogger("jpyoftheday")
handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter('%(asctime)s %(name)s %(filename)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s'))
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


gw = YfinaceExchangeRateGw()
usecase = GetJpyOfTheDayUsecase(gw)
presenter = GetJpyOfTheDayPresenter()
view = GetJpyOfTheDayViewImpl()

controller = GetJpyOfTheDayController(usecase, presenter, view)


def display_usage():
    print("")
    print("Type date(eg: 2025-04-26)")
    print("Type 'q' to exit")
    print("")

debug_prompt = ""
print("")
print("##############################")
print("    USD to JPY converter")
print("##############################")
display_usage()
while True:
    user_input = input(f"{debug_prompt}Input date: ")
    if user_input == "q":
        print("")
        exit()
    if user_input == "v":
        if handler.level == 10:
            handler.setLevel(INFO)
            debug_prompt = ""
        else:
            handler.setLevel(DEBUG)
            debug_prompt = "(VERBOSE_MODE)"
        print("")
        continue
    if user_input == "h":
        display_usage()
        continue
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


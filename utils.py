from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(data):
    currently_year = datetime.now().year
    first_cup = data["first_cup"].split("-")[0]
    num_copas = (currently_year - int(first_cup)) // 4

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if int(first_cup) % 4 != 2 or int(first_cup) < 1930:
        raise InvalidYearCupError("there was no world cup this year")

    if data["titles"] > num_copas:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

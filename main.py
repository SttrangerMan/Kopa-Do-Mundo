from utils import data_processing


data = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}

print(data_processing(data))
# ImpossibleTitlesError: impossible to have more titles than disputed cups

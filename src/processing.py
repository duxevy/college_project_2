from typing import Any

opers = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def get_date(operation: dict) -> Any:
    return operation["date"]


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует по статусу
    :param operations:
    :param state:
    :return:
    """
    transactions = []
    for operation in operations:
        if operation["state"] == state:
            transactions.append(operation)
    return transactions


def sort_by_date(operations: list[dict], direction: bool = True) -> list[dict]:
    """
    Сортирует по дате
    :param operations:
    :param direction:
    :return:
    """
    return sorted(operations, key=get_date, reverse=direction)


# print(filter_by_state(opers, state="CANCELED"))
# print(sort_by_date(opers, direction=False))

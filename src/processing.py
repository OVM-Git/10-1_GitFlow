from datetime import datetime
from typing import List, Dict


def filter_by_state(data_basu: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_basu: Список словарей с транзакциями.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [data_basu for data_basu in data_basu if data_basu.get('state') == state]

def sort_by_date(data_basu: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data_basu: Список словарей с транзакциями.
    :param reverse: Если True, сортировка по убыванию (по умолчанию True).
    :return: Отсортированный список словарей.
    """
    return sorted(data_basu, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)

# Примеры использования функций:

data_basu = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
'''
# Фильтрация по состоянию 'EXECUTED'
filtered_executed = filter_by_state(data_basu)
print(filtered_executed)
# Вывод:
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Фильтрация по состоянию 'CANCELED'
filtered_canceled = filter_by_state(data_basu, 'CANCELED')
print(filtered_canceled)
# Вывод:
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Сортировка по убыванию даты
sorted_desc = sort_by_date(data_basu)
print(sorted_desc)
# Вывод:
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Сортировка по возрастанию даты
sorted_asc = sort_by_date(data_basu, reverse=False)
print(sorted_asc)
# Вывод:
# [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
'''
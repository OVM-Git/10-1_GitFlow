import pytest
from datetime import datetime
from src.widget import mask_account_card, get_date  # Замените your_module на имя вашего модуля


# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_info, expected", [
    ("Счет 1234567890123456", "Счет **3456"),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
    ("Счет 1234", "Счет **1234"),  # Крайний случай - короткий номер счета
    ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),  # Неизвестный тип карты
])
def test_mask_account_card(input_info, expected):
    assert mask_account_card(input_info) == expected


# Тесты для функции get_date
@pytest.mark.parametrize("input_date, expected", [
    ("2023-05-15T10:30:00", datetime(2023, 5, 15, 10, 30, 0)),
    ("2020-12-31T23:59:59", datetime(2020, 12, 31, 23, 59, 59)),
    ("2018-01-01T00:00:00", datetime(2018, 1, 1, 0, 0, 0)),
])
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("неправильная дата")
    with pytest.raises(ValueError):
        get_date("2023-13-01T00:00:00")  # Несуществующий месяц
    with pytest.raises(ValueError):
        get_date("2023-02-30T00:00:00")  # Несуществующий день
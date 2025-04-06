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
    ("2023-01-01T00:00:00", "01.01.2023"),
    ("2022-12-31T23:59:59", "31.12.2022"),
])
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected  # Теперь проверяет строк


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("неправильная дата")
    with pytest.raises(ValueError):
        get_date("2023-13-01T00:00:00")  # Несуществующий месяц
    with pytest.raises(ValueError):
        get_date("2023-02-30T00:00:00")  # Несуществующий день